from django import forms


class OrderCreateForm(forms.Form):
    contact_info = forms.CharField(
        label="Additional info",
        required=True,
        widget=forms.TextInput,
        help_text="Please insert your delivery address and phone number if it's different from you account's data.",
    )
