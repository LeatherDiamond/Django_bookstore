from catalog.models import AppUser
from django.forms import (
    ModelForm,
    CharField,
)


class ProfileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ("country", "city", "address", "reserve_address", "index"):
            self.fields[field].widget.attrs["disabled"] = True
            self.fields[field].widget.required = False

            def clean(name=field):
                if self.instance and self.instance.pk:
                    return getattr(self.instance, name)
                else:
                    return self.cleaned_data[name]

            setattr(self, "clean_%s" % field, clean)

    country = CharField(disabled=True)
    city = CharField(disabled=True)
    address = CharField(disabled=True)
    reserve_address = CharField(disabled=True, required=False)
    index = CharField(disabled=True, required=False)

    class Meta:
        model = AppUser
        fields = (
            "email",
            "name",
            "surname",
            "phone",
            "country",
            "city",
            "address",
            "reserve_address",
            "additional_info",
            "index",
        )
