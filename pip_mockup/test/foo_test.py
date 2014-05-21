from ..foo import myFunction
import unittest


def test_return():
    assert myFunction('fred') == "Foo::myFunction says fred"
