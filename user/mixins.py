from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect


class SuperuserRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)