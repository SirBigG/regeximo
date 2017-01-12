from django import forms
from django.utils.text import normalize_newlines, mark_safe

from core.logs.models import SiteLog


class LogParsingForm(forms.Form):
    site_name = forms.CharField()
    file = forms.FileField()

    class Meta:
        widgets = {
            'site_name': forms.TextInput(attrs={'class': "form-control input-lg"}),
            'file': forms.FileInput(attrs={'class': "form-control input-lg"})
        }

    def save(self):
        to_save = [
            SiteLog(site_name=self.cleaned_data['site_name'],
                    text=_line) for _line in self.cleaned_data['file'].readlines()
            if mark_safe(normalize_newlines(str(_line)).replace('\n', ' '))]
        SiteLog.objects.bulk_create(to_save)
