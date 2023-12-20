from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import (
    HttpResponseRedirect,
)
from django.shortcuts import (
    get_object_or_404,
    render,
)
from django.urls import reverse_lazy
from django.views import generic

from order.models import (
    Order,
    Status,
)


class AdminPortalView(LoginRequiredMixin, PermissionRequiredMixin, generic.TemplateView):
    permission_required = "product_card.view_book"
    login_url = "home_page:login"

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "admin_portal/portal_detail.html",
            context={
                "user": request.user,
                "orders": Order.objects.select_related("cart"),
                "status_created": Status.objects.get(pk=1),
                "status_updated": Status.objects.get(pk=2),
                "status_cancelled": Status.objects.get(pk=3),
            },
        )


class StatusView(generic.UpdateView):
    def post(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        order = get_object_or_404(Order, pk=pk)
        status = self.request.POST.get("status")
        order.status_id = status
        order.save()
        return HttpResponseRedirect(reverse_lazy("admin_portal:admin_portal"))
