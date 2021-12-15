import pytest
from types import SimpleNamespace

from report2sqaaas_plugins_{{cookiecutter.plugin_name}}.main import {{cookiecutter.plugin_class_name}}


@pytest.fixture
def {{cookiecutter.plugin_name}}_stdout():
    # FIXME Return a sample tool's stdout as string
    return ""

@pytest.fixture
def validator_opts({{cookiecutter.plugin_name}}_stdout):
    class_args = {
        'validator': '{{cookiecutter.plugin_name}}',
        'stdout': {{cookiecutter.plugin_name}}_stdout
    }
    return SimpleNamespace(**class_args)


@pytest.fixture
def validator(validator_opts):
    return {{cookiecutter.plugin_class_name}}(validator_opts)


@pytest.mark.dependency()
def test_is_validate_method_defined(validator_opts):
    assert LicenseeValidator(validator_opts).validate()


@pytest.mark.dependency(depends=["test_is_validate_method_defined"])
def test_validate_method_output(validator):
    result = validator.validate()
    assert type(result) is dict
    assert 'valid' in list(result)
