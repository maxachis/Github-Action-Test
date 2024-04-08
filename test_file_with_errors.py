def test_function_no_type_hinting(a, b):
    """
    This test function includes a doc string but includes no type hinting
    """


def test_function_no_docstring(a: int, b: str) -> list:
    return []


def test_function_no_errors(a: int, b: str) -> list:
    """
    This has both docstring and type hinting, and should not produce errors in mypy or pydocstring
    :param a:
    :param b:
    :return:
    """
    return []
