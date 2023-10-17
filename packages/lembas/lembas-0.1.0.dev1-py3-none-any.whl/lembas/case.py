from __future__ import annotations

import inspect
import itertools
import logging
import types
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Iterator
from functools import WRAPPER_ASSIGNMENTS
from functools import cached_property
from pathlib import Path
from typing import Any
from typing import ClassVar
from typing import Generic
from typing import Optional
from typing import TypeVar

import toml

from lembas.logging import logger
from lembas.param import InputParameter

__all__ = ["Case", "CaseList", "step"]

LEMBAS_CASE_TOML_FILENAME = "lembas-case.toml"

TCase = TypeVar("TCase", bound="Case")
RawCaseStepMethod = Callable[[TCase], None]


class CaseStep:
    def __init__(
        self,
        func: RawCaseStepMethod,
        *,
        condition: Callable[[Any], bool] | None = None,
        requires: str | Iterable[str] | None = None,
    ):
        self._func = func
        self._condition = condition
        self.requires = (
            [requires] if isinstance(requires, str) else list(requires or [])
        )

    @cached_property
    def name(self) -> str:
        """The name of the case step."""
        return self._func.__name__

    def __call__(self, instance: Case) -> None:
        if self._condition is None or self._condition(instance):
            return self._func(instance)
        return None

    def __get__(self, instance: Any, cls: Any) -> types.MethodType:
        """We need to implement __get__ so that the `CaseStep` can be used as a method.

        Without doing this, Python will treat it as a normal attribute access, rather
        than as a descriptor.

        """
        return types.MethodType(self, instance)


class Case:
    """Base case for all cases.

    When constructing a new case, all assigned ``InputAttribute`` values can be set via keyword arguments.

    """

    _steps: ClassVar[dict[str, CaseStep]]

    def __init_subclass__(cls, **kwargs: Any):
        cls._steps = {
            name: method
            for name, method in cls.__dict__.items()
            if isinstance(method, CaseStep)
        }

    def __init__(self, **kwargs: Any):
        self._completed_steps: set[str] = set()
        for name, value in kwargs.items():
            setattr(self, name, value)

    def __str__(self) -> str:
        cls = self.__class__
        lines = [f"{cls.__name__}:"]
        for name, value in cls.__dict__.items():
            if isinstance(value, InputParameter):
                lines.append(f"  - {name}: {getattr(self, name)}")
        return "\n".join(lines)

    @staticmethod
    def log(msg: str, *args: Any, level: int = logging.INFO) -> None:
        """Log a message to the logger."""
        logger.log(level, msg, *args)

    @property
    def fully_resolved_name(self) -> str:
        """The fully-resolved import path of the case handler."""
        cls = self.__class__
        mod = inspect.getmodule(cls)
        mod_prefix = mod.__name__ + "." if mod is not None else ""
        return mod_prefix + cls.__qualname__

    @cached_property
    def case_dir(self) -> Optional[Path]:
        f"""An optional property that can be set for a subclass.

        If set, the `{LEMBAS_CASE_TOML_FILENAME}` file will be written in this directory.

        """
        return None

    @cached_property
    def relative_case_dir(self) -> Optional[Path]:
        """Return a case directory relative to current working directory if possible.

        If the case directory is not a subdirectory of current working directory, the absolute
        path is returned.

        """
        if self.case_dir is None:
            return None

        try:
            return self.case_dir.relative_to(Path.cwd())
        except ValueError:
            return self.case_dir

    @property
    def inputs(self) -> dict[str, Any]:
        """A mapping of the name of each InputAttribute to its value."""
        attr_names = (
            k
            for k, v in self.__class__.__dict__.items()
            if isinstance(v, InputParameter) and v.include_in_inputs_dict
        )
        return {n: getattr(self, n) for n in attr_names}

    @property
    def _sorted_steps(self) -> Iterator[CaseStep]:
        """Yield the case steps in order, with proper sorting of dependencies."""
        steps = dict(self._steps)
        while steps:
            for name, step in steps.items():
                if not step.requires or (set(step.requires).issubset(self._completed_steps)):  # type: ignore
                    yield steps.pop(name)
                    self._completed_steps.add(name)
                    break

    def _write_lembas_file(self) -> None:
        """Write a file in the case directory specifying the case handler and all input values used."""
        if self.relative_case_dir is None:
            return None

        case_summary_file = self.relative_case_dir / LEMBAS_CASE_TOML_FILENAME
        case_summary_file.parent.mkdir(parents=True, exist_ok=True)

        self.log("Writing case summary to: %s", case_summary_file)
        contents = {
            "lembas": {"inputs": self.inputs, "case-handler": self.fully_resolved_name}
        }
        with case_summary_file.open("w") as fp:
            toml.dump(contents, fp)

    def run(self) -> None:
        """Run the case.

        If this method is not overridden, the default behavior is to run all the methods
        decorated with ``@step``.

        """
        self.log("Running %s", self)
        self._write_lembas_file()
        for step_method in self._sorted_steps:
            step_method(self)


class CaseList(Generic[TCase]):
    """A generic collection of ``Case`` objects, and utility methods to create and run them.

    Args:
        cases: An optional iterable of ``Case`` objects used to initialize the ``CaseList``.

    """

    def __init__(self, cases: Iterable[TCase] | None = None):
        self._cases: list[TCase] = list(cases or ())

    def add(self, case: TCase) -> TCase:
        """Add a case to the list:

        Args:
            case: The case to add.

        Returns:
            The case that was added.

        """
        self._cases.append(case)
        return case

    def add_cases_by_parameter_sweep(
        self, case_class: type[TCase], **kwargs: Any
    ) -> None:
        """Add a number of cases by performing a parameter sweep using the Cartesian product.

        Args:
            case_class: The type of case to construct.
            kwargs: Any parameters to pass to the case constructors. If iterable values are provided,
                they will be used when performing the parameter sweep via ``itertools.product``.

        """
        # Ensure all kwargs have iterable values by wrapping scalars and strings
        for key, value in kwargs.items():
            if isinstance(value, str) or not isinstance(value, Iterable):
                kwargs[key] = [value]

        for values in itertools.product(*kwargs.values()):
            new_kwargs = {k: v for k, v in zip(kwargs.keys(), values)}
            case = case_class(**new_kwargs)
            self.add(case)

    def run_all(self) -> None:
        """Run all the cases."""
        for case in self._cases:
            case.run()

    def __contains__(self, item: TCase) -> bool:
        return item in self._cases

    def __len__(self) -> int:
        return len(self._cases)

    def __iter__(self) -> Iterator[TCase]:
        for case in self._cases:
            yield case


def step(
    method: RawCaseStepMethod | None = None,
    /,
    condition: Callable[[Any], bool] | None = None,
    requires: str | Iterable[str] | None = None,
) -> Any:
    """A decorator to define steps to be performed when running a `Case`.

    The step should not return a value.

    Args:
        method: The decorator may be used without any arguments, in which case the defaults
            will be used.
        condition: an optional callable which can be used to determine whether the step should run.
            It will receive the `Case` instance as its only argument, and must return a boolean
            which, if True, the step will run. Otherwise, it will be skipped.
        requires: An iterable of dependent steps on which this one depends, or a single string.

    Usage:
        .. code-block::

            class MyCase(Case):
                @step(condition=lambda case: case.case_dir.exists())
                def some_analysis_step(self):
                    # do something

    """

    def decorator(f: RawCaseStepMethod) -> CaseStep:
        new_method = CaseStep(f, condition=condition, requires=requires)
        # This is largely a replica of functools.wraps, which doesn't seem to work
        for attr in WRAPPER_ASSIGNMENTS:
            setattr(new_method, attr, getattr(f, attr, None))
        return new_method

    if method is not None:  # handle case where there are no arguments
        return decorator(method)
    return decorator
