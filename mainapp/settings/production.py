# its for base actually

import os
import json
from django.core.exceptions import ImproperlyConfigured


with open(os.environ.get('COMPLETEAPP_CONFIG')) as f:
    configs = json.loads(f.read())


def get_env_var(setting, configs=configs):
    try:
        val = configs[setting]
        if val == 'True':
            val = True
        elif val == 'False':
            val = False
        return val
    except KeyError:
        error_msg = "ImproperlyConfigured: Set {0} environmentvariable".format(setting)
        raise ImproperlyConfigured(error_msg)


# get secret key
SECRET_KEY = get_env_var("SECRET_KEY")
