from django.utils.functional import cached_property
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.core.exceptions import PermissionDenied, BadRequest


class PrimeMixin:
    @property
    def get_numb(self):
        try:
            return self.request.resolver_match.kwargs["numb"]
        except KeyError:
            raise BadRequest(
                "The number to check for prime is not given. For example /blog/check-prime/<number>/"
            )

    @cached_property
    def is_prime(self):
        """Check if a number is a prime number

        Args:
            number (int): The number to check if prime

        Returns:
            result (bool): True or False
        """
        result = True
        for i in range(2, self.get_numb // 2 + 1):
            if self.get_numb % i == 0:
                result = False
                break

        return result


def pagination(request, object_list, page_limit=2):
    paginator = Paginator(object_list, page_limit)
    page = request.GET.get("page")
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)
    return results


class AdminRequiredMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_staff:
            return queryset
        raise PermissionDenied


# def check_if_admin(request: HttpRequest) -> Optional[HttpRequest]:
#     if request.user.is_staff:
#         return request
#     raise PermissionDenied


class SearchMixin:
    def get_queryset(self):
        queryset = super().get_queryset()

        q = self.request.GET.get("q")
        if q:
            return queryset.filter(title__icontains=q)
        return queryset
