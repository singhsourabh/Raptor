from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlparse


def validate_url(value):
    parsed_url = urlparse(value)
    if not parsed_url.netloc == 'erp.aktu.ac.in':
        raise ValidationError(
            _('Please provide a valid url'), code='condition-failed'
        )


class CrawlDemoForm(forms.Form):
    url = forms.URLField(validators=[validate_url])
