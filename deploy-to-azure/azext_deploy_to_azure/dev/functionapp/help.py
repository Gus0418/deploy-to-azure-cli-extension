# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps
from azext_deploy_to_azure.dev.common.locale.locale_helper import get_messages


def load_functionapp_help():
    _msgs = get_messages()
    _group_short = _msgs.HELP_FUNCTIONAPP_GROUP_SHORT if _msgs else 'Commands to manage Azure Functions app.'
    _up_short = _msgs.HELP_FUNCTIONAPP_UP_SHORT if _msgs else 'Deploy to Azure Functions via GitHub actions.'
    _ex1_name = (_msgs.HELP_FUNCTIONAPP_EX1_NAME if _msgs
                 else 'Deploy/Setup GitHub action for a GitHub Repository to Azure Function - Run interactive mode')
    _ex2_name = (_msgs.HELP_FUNCTIONAPP_EX2_NAME if _msgs
                 else 'Deploy/Setup GitHub Action for locally checked out GitHub Repository to Azure Function')
    _ex2_text = (_msgs.HELP_FUNCTIONAPP_EX2_TEXT if _msgs
                 else 'Repository name/url (--repository) will be detected from the local git repository')
    _ex3_name = (_msgs.HELP_FUNCTIONAPP_EX3_NAME if _msgs
                 else 'Deploy/Setup GitHub action for a GitHub Repository to Azure Function')

    helps['functionapp app'] = f"""
    type: group
    short-summary: {_group_short}
    long-summary:
    """

    helps['functionapp app up'] = f"""
    type: command
    short-summary: {_up_short}
    long-summary:
    examples:
      - name: {_ex1_name}
        text: |
          az functionapp app up

      - name: {_ex2_name}
        text: |
          {_ex2_text}
          az functionapp app up --app-name AzFunctionPythonPreProd

      - name: {_ex3_name}
        text: |
          az functionapp app up --app-name AzFunctionPythonPreProd --repository https://github.com/azure/deploy-functions
    """
