from django import forms

from core.logs.models import SiteLog


class LogParsingForm(forms.Form):
    site_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control input-lg"}))
    file = forms.FileField(widget=forms.FileInput(attrs={'class': "form-control"}))

    def save(self):
        i = 0
        to_save = list()
        site_name = self.cleaned_data['site_name']
        for _line in self.cleaned_data['file'].readlines():
            _line = _line.decode("utf-8").replace('\n', '')
            if _line:
                to_save.append(SiteLog(site_name=site_name, text=_line))
            if i == 100:
                SiteLog.objects.bulk_create(to_save)
                to_save = []
                i = 0
            i += 1
        else:
            SiteLog.objects.bulk_create(to_save)


class SearchLogForm(forms.Form):
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    regex = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    text = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
