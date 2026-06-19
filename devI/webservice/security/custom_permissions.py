from rest_framework import permissions


class CustomPermissions(permissions.BasePermission):

    perms_maps = {
        "GET": ["%(app_label)s.view_%(model_name)s"],
        "POST": ["%(app_label)s.add_%(model_name)s"],
        "PUT": ["%(app_label)s.change_%(model_name)s"],
        "DELETE": ["%(app_label)s.delete_%(model_name)s"],
        "OPTIONS": [],
        "PATCH": ["%(app_label)s.change_%(model_name)s"],
    }

