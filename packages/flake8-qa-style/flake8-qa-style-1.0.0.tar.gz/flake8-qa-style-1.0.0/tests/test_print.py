from flake8_plugin_utils import assert_error

from flake8_qa_style.errors import Print
from flake8_qa_style.visitors.call_checkers import PrintChecker
from flake8_qa_style.visitors.function_call_visitor import FunctionCallVisitor


def test_call_print():
    FunctionCallVisitor.deregister_all()
    FunctionCallVisitor.register_checker(PrintChecker)
    code = """
    print('asdasd')
    """
    assert_error(FunctionCallVisitor, code, Print)


def test_call_pp():
    FunctionCallVisitor.deregister_all()
    FunctionCallVisitor.register_checker(PrintChecker)
    code = """
    pp('asdasd')
    """
    assert_error(FunctionCallVisitor, code, Print)
