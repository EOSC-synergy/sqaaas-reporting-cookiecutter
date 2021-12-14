## #1 Generate the SQAaaS reporting plugin's module

### Use cookiecuttter template
If not already in your environment, install 
[cookiecutter](https://cookiecutter.readthedocs.io/) executable:
```console
$ pip install cookiecutter
```

Now you are ready to create the validator plugin module:
```console
$ cookiecutter https://github.com/EOSC-synergy/sqaaas-reporting-cookiecutter
```

### The module structure
The following folder structure is created by cookiecutter:
```console
└── {{cookiecutter.criterion}}_{{cookiecutter.plugin_name}}
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── README.md
    ├── report2sqaaas_plugins_{{cookiecutter.plugin_name}}
    │   ├── __init__.py
    │   ├── main.py
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── test-requirements.txt
    └── tests
        └── test_validator.py
```

### A note about testing
A test-driven development (TDD) approach is followed in order to make sure that
the main validator class, `validate()`, has been defined. Thus, the generated 
module provides two test cases out of the box:
- `validate()` method has been implemented.
- `validate()` method returns a dictionary with the `valid` flag.

*Note: the plugin developer needs to provide a sample output of the tool* (within the
fixture `<tool_name>_stdout`)

## #2 Implement the validate() method
In order to have a working plugin, the **`validate()` method has to be implemented**
within the validator class:
 - *Expected output*: dictionary with the results of the validation through the boolean
   variable `valid`. The most simple definition of the `validate()` method could be:
   ```python
   class FooValidator(BaseValidator):
       valid = False
       
       @staticmethod
       def validate():
           return {'valid': self.valid}
   ```
