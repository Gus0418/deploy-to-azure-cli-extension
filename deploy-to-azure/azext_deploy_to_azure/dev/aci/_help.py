# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=consider-using-f-string
from knack.help_files import helps
from azext_deploy_to_azure.dev.common.locale.locale_helper import get_messages


def load_aci_help():
    _msgs = get_messages()
    _group_short = _msgs.HELP_ACI_GROUP_SHORT if _msgs else 'Commands to Manage Azure Container Instances App'
    _up_short = (_msgs.HELP_ACI_UP_SHORT if _msgs
                 else 'Deploy to Azure Container Instances using GitHub Actions. '
                      'Refer to https://aka.ms/aci-deploy-action for more information.')

    helps['container app'] = """
    type: group
    short-summary: {group_short}
    long-summary:
    """.format(group_short=_group_short)

    helps['container app up'] = """
    type: command
    short-summary: {up_short}
    long-summary:
    """.format(up_short=_up_short)
