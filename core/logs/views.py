from django.views.generic import FormView
from django.http import HttpResponseRedirect

from .forms import LogParsingForm


class LogParsingFormView(FormView):
    form_class = LogParsingForm
    template_name = 'logs/log_parse_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(redirect_to=self.success_url)
