from typing import Optional
import functools
from django.http import HttpRequest
from django.core.exceptions import PermissionDenied


def check_if_admin(request: HttpRequest) -> Optional[HttpRequest]:
    if request.user.is_staff:
        return request
    raise PermissionDenied


def admin_required(view_func):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        request = check_if_admin(request)
        return view_func(request, *args, **kwargs)

    return wrapper
