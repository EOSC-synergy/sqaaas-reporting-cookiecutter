# Steps to implement a SQAaaS reporting plugin

## #1 Generate the plugin's Python module

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

### The plugin module structure
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


# Recommended workflow

1. Fork https://github.com/eosc-synergy/sqaaas-reporting-plugins, clone it & chdir to it.
2. Create a Python virtualenv to install the dependencies:
   ```console
   $ python3 -m venv venv
   $ source venv/bin/activate
   $ pip install cookiecutter
   ```
3. Run cookiecutter as in previous step #1.
   - This will place the new validator plugin within the root path of the fork repository.
   ```console
   $ cookiecutter https://github.com/EOSC-synergy/sqaaas-reporting-cookiecutter
   ```
4. Chdir to the root path of the generated plugin (`<criterion_name>_<tool_name>` folder)
5. Install plugin dependencies
   ```console
   $ pip install -r requirements.txt
   $ pip install -r test-requirements.txt
   ```
6. Follow the TDD approach by running `pytest` to double check that the `validate()` method
   is not yet implemented.
   ```console
   $ pytest -svv
   ```
7. Implement the `validate()` method taking into account the remarks from step #2.
8. Try your new validator using `report2sqaaas` CLI.
   - First you need to generate the output from the tool being validated.
   ```console
   $ # Generate the <tool_name> output & store it in <file_name>
   $ report2sqaaas <plugin_name> <file_name>
   ```
9. Once the plugin is doing the expected job, rerun the tests:
   ```console
   $ pytest -svv
   ```
10. Add & commit the plugin within the fork.
12. Create a PR to the upstream repo (from where the fork has been created).
