from django import forms
from .models import User
from django.core.validators import URLValidator, RegexValidator
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from urllib.parse import urlparse


def validate_rollno(value):
    if not re.match('\d{10}', str(value)):
        raise ValidationError(
            _('%(value)s is not a valid roll no'),
            params={'value': value}, code='condition-failed'
        )


def validate_url(value):
    parsed_url = urlparse(value)
    if not parsed_url.netloc == 'erp.aktu.ac.in':
        raise ValidationError(
            _('Please provide a valid url'), code='condition-failed'
        )


class CrawlForm(forms.Form):
    roll_no = forms.IntegerField(
        validators=[validate_rollno])
    url = forms.URLField(validators=[validate_url])
