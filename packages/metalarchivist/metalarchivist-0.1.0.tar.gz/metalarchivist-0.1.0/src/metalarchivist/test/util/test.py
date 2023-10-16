import sys
import unittest
import importlib.util
from types import ModuleType
from enum import Enum


class Submodule(Enum):
    EXPORT = 'metalarchivist.export', './src/metalarchivist/export/__init__.py'
    REPORT = 'metalarchivist.report', './src/metalarchivist/report/__init__.py'


def run_test_cases():
    unittest.main(argv=[''], verbosity=2)


def prepare_submodule(submodule: Submodule) -> ModuleType:
    submodule_name, submodule_path = submodule.value
    spec = importlib.util.spec_from_file_location(submodule_name, submodule_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[submodule_name] = module
    spec.loader.exec_module(module)

    return module
