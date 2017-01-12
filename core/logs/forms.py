from django import forms

from core.logs.models import SiteLog


class LogParsingForm(forms.Form):
    site_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control input-lg"}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control"}))

    def save(self):
        to_save = [
            SiteLog(site_name=self.cleaned_data['site_name'],
                    text=_line) for _line in self.cleaned_data['file'].readlines()
            if str(_line).replace('\n', '')]
        SiteLog.objects.bulk_create(to_save)


class SearchLogForm(forms.Form):
    name = forms.CharField(required=False)
    regex = forms.CharField(required=False)
    text = forms.CharField(required=False)
