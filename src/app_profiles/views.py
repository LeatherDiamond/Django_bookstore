from django.http import (
    HttpResponseRedirect,
)
from django.shortcuts import (
    get_object_or_404,
    render,
)
from django.urls import reverse_lazy
from django.views import generic

from app_profiles.forms import ProfileForm
from order.models import (
    Order,
    Status,
)


class ProfileView(generic.DetailView, generic.UpdateView):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "app_profiles/profile_view.html",
            context={
                "user": request.user,
                "orders": Order.objects.select_related("cart").filter(user=request.user),
                "form": ProfileForm(instance=request.user),
            },
        )

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy("app_profiles:profile_view"))
        return render(
            request,
            "app_profiles/profile_view.html",
            context={
                "user": request.user,
                "orders": Order.objects.select_related("cart").filter(user=request.user),
                "form": form,
            },
        )


class CancelOrderView(generic.UpdateView):
    def post(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        order = get_object_or_404(Order, pk=pk)
        action = self.request.POST.get("submit", "cancel")
        status_name = "Cancelled" if action == "cancel" else "Updated"
        status, _ = Status.objects.get_or_create(name=status_name)
        order.status = status
        order.save()
        return HttpResponseRedirect(reverse_lazy("app_profiles:profile_view"))


class ContactInfoView(generic.UpdateView):
    def post(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        order = get_object_or_404(Order, pk=pk)
        contact_info = self.request.POST.get("contact_info", "")
        order.contact_info = contact_info
        order.save()
        return HttpResponseRedirect(reverse_lazy("app_profiles:profile_view"))
