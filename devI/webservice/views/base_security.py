from rest_framework import permissions, authentication
from webservice.security import CustomPermissions, TokenAuthentication


class BaseSecurity:
    permission_classes = [permissions.IsAuthenticated, CustomPermissions]
    authentication_classes = [authentication.SessionAuthentication, TokenAuthentication]
