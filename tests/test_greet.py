import importlib.util
import unittest
from pathlib import Path


def _load_greet():
    greet_path = Path(__file__).resolve().parents[1] / "src" / "greet.py"
    spec = importlib.util.spec_from_file_location("greet_under_test", greet_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"cannot load {greet_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.greet


greet = _load_greet()


class TestGreet(unittest.TestCase):
    def test_greeting(self) -> None:
        self.assertEqual(greet("Swarm"), "Hello, Swarm!")


if __name__ == "__main__":
    unittest.main()
