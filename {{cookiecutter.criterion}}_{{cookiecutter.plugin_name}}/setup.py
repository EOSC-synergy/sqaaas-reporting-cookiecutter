from setuptools import find_packages
from setuptools import setup


setup(
    name='report2sqaaas-plugin-{{cookiecutter.plugin_name}}',
    version='1.0.0',
    description='Output validator for the {{cookiecutter.tool_name}} tool',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/eosc-synergy/sqaaas-reporting-plugins',
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: GNU General Public License v3 or later '
         '(GPLv3+)'),
        'Environment :: Plugins',
        'Development Status :: 3 - Alpha',
    ],
    packages=find_packages(),
    entry_points={
        'sqaaas.validators': [
            '{{cookiecutter.plugin_name}} = report2sqaaas_plugins_{{cookiecutter.plugin_name}}.main:{{cookiecutter.plugin_class_name}}',
        ],
    },
)
