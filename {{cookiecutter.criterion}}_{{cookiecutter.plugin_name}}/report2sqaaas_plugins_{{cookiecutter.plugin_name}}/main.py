# SPDX-FileCopyrightText: Copyright contributors to the Software Quality Assurance as a Service (SQAaaS) project.
#
# SPDX-License-Identifier: GPL-3.0-or-later

import logging

from report2sqaaas import utils as sqaaas_utils


logger = logging.getLogger('sqaaas.reporting.plugins.{{cookiecutter.plugin_name }}')


class {{cookiecutter.plugin_class_name}}(sqaaas_utils.BaseValidator):
    valid = False
    {%- if cookiecutter.threshold %}
    threshold = {{ cookiecutter.threshold }}
    {%- endif %}

    {%- if cookiecutter.has_additional_cli_args.lower() in ['yes'] %}
    @staticmethod
    def populate_parser(parser):
        """Additional CLI arguments for the validator

        Example of '--verbosity' flag:

            parser.add_argument(
                '--verbosity',
                help='Increase output verbosity'
            )

        """
        pass
    {%- endif %}
