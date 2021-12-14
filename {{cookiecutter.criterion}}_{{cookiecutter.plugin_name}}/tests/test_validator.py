import pytest
from types import SimpleNamespace

from report2sqaaas_plugins_{{cookiecutter.plugin_name}}.main import {{cookiecutter.plugin_class_name}}


@pytest.fixture
def {{cookiecutter.tool_name}}_stdout():
    # FIXME Return a sample tool's stdout as string
    return ""

@pytest.fixture
def validator({{cookiecutter.tool_name}}_stdout):
    class_args = {
        'validator': '{{cookiecutter.plugin_name}}',
        'stdout': {{cookiecutter.tool_name}}_stdout
    }
    opts = SimpleNamespace(**class_args)
    return {{cookiecutter.plugin_class_name}}(opts)


def test_is_validate_method_defined(validator):
    try:
        validator.validate()
    except TypeError:
        pytest.fail('{{cookiecutter.plugin_class_name}} class does not implement validate() method')


def test_is_validate_method_output(validator):
    result = validator.validate()
    assert type(result) is dict
    assert 'valid' in list(result)
