from utils.BearerAuthentication import BearerTokenAuthentication
from oauth2_provider.backends import OAuth2Backend

class UserUtils:

    def get_user(request=None):
        if request is not None:
            return OAuth2Backend().authenticate(request)
        else:
            return None