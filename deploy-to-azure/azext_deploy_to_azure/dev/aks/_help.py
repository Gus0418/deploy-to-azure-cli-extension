# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps
from azext_deploy_to_azure.dev.common.locale.locale_helper import get_messages


def load_aks_help():
    _msgs = get_messages()
    _group_short = _msgs.HELP_AKS_GROUP_SHORT if _msgs else 'Commands to manage AKS app.'
    _up_short = _msgs.HELP_AKS_UP_SHORT if _msgs else 'Deploy to AKS via GitHub actions.'

    helps['aks app'] = f"""
    type: group
    short-summary: {_group_short}
    long-summary:
    """

    helps['aks app up'] = f"""
    type: command
    short-summary: {_up_short}
    long-summary:
    """
