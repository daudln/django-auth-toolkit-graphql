from django.contrib.auth.backends import BaseBackend
from oauth2_provider.models import AccessToken
from django.utils import timezone


class BearerTokenAuthentication(BaseBackend):
    def authenticate_header(self, request):
        return 'Bearer'

    @staticmethod
    def authenticate(request):
        try:
            bearer_token = request.META['HTTP_AUTHORIZATION'].split(' ')[1]
            token = AccessToken.objects.filter(token=bearer_token, expires__gt=timezone.now()).first()
            
            if token is not None:
                return token.user
            
            else:
                return None
            
        except AccessToken.DoesNotExist:
            return None
        
        except Exception as e:
            return None
