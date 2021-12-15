## #1 Generate the SQAaaS reporting plugin's module

### Use cookiecuttter template
If not already in your environment, install 
[cookiecutter](https://cookiecutter.readthedocs.io/) executable:
```console
$ pip install cookiecutter
```

Now you are ready to create the validator plugin module using the 
template from this repository:
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
the `validate()` method has been defined in the validator class. Thus, the generated 
module provides two test cases out of the box:
- `validate()` method has been implemented.
- `validate()` method returns a dictionary with the `valid` flag.

*Note: the plugin developer needs to provide a sample output of the tool* (within the
fixture `<tool_name>_stdout`)

## #2 Implement the validate() method
The `validate()` method must:
1. Implemented in the validator class.
2. Return a dictionary* containing *at least* the `valid` key, with a boolean value
   (True|False) that marks the validation as successful or unsuccessful.
   
The most simple example could be:
```python
class FooValidator(BaseValidator):
    valid = False
       
    @staticmethod
    def validate():
       return {'valid': self.valid}
```

### Some remarks when implementing validate() method
- The *validator class* has the following *set of attributes* that can be used when
  implementing the `validate()` method
  - `name`: validator name (available as `self.name`)
  - `opts`: object that contains the attributes provided when the class is 
    instantiated. Those are the same as the input arguments of the
    [report2sqaaas](https://github.com/eosc-synergy/reporting-sqaaas) module,
    such as `validator` (available as class attribute `self.opts.validator`),
    `stdout` (`self.opts.stdout`) or `threshold` (`self.opts.threshold`).
- The validator's test cases require a sample output of the tool being validated
  in order to successfully pass the `test_validate_method_output` test. The *output
  shall be placed within the pytest fixture `<tool_name>_stdout()`* in
  [test_validator.py](%7B%7Bcookiecutter.criterion%7D%7D_%7B%7Bcookiecutter.plugin_name%7D%7D/tests/test_validator.py).
  The generated plugin will contain 
  [instructions on how to run the tests](%7B%7Bcookiecutter.criterion%7D%7D_%7B%7Bcookiecutter.plugin_name%7D%7D/README.md#testing).
    
## #3 Contribute to reporting-sqaaas-plugins
Once you have implemented the `validate()` method and the tests are passing, you should
contribute to the existing set of validator plugins of the SQAaaS reporting component.
To this end, create a pull request to
[reporting-sqaaas-plugins](https://github.com/eosc-synergy/sqaaas-reporting-plugins).

1. Fork https://github.com/eosc-synergy/sqaaas-reporting-plugins and clone it
2. Run cookiecutter as in previous [step #1](use-cookiecuttter-template)
   - This will place the new validator plugin within the root path of the fork repository.
3. Add & commit the changes to your fork
4. Create a PR to the upstream repo (from where the fork has been created)
