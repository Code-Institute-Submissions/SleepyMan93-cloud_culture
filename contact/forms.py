from django import forms

from .models import OrderInquiry


class OrderInquiryForm(forms.ModelForm):

    class Meta:
        model = OrderInquiry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)