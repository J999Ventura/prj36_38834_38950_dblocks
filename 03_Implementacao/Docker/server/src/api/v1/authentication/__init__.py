'''
   authentication_routes init
'''

from api.v1.authentication.base import Praetorian  # noqa
from api.v1.authentication.exceptions import PraetorianError  # noqa
from api.v1.authentication.decorators import (  # noqa
    auth_required,
    roles_required,
    roles_accepted,
)
from api.v1.authentication.utilities import (  # noqa
    current_user,
    current_user_id,
    current_rolenames,
    current_custom_claims,
)
