# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

import os


def is_zh_tw():
    """Return True when the runtime locale is Traditional Chinese (zh_TW / zh_Hant)."""
    for env_var in ('LANG', 'LC_ALL', 'LC_MESSAGES', 'LANGUAGE'):
        value = os.environ.get(env_var, '')
        if value.startswith('zh_TW') or value.startswith('zh_Hant'):
            return True
    return False


def get_messages():
    """Return the messages module for the current locale."""
    if is_zh_tw():
        from azext_deploy_to_azure.dev.common.locale.zh_TW import messages
        return messages
    return None
