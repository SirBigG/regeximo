from django.views.generic import FormView, ListView
from django.http import HttpResponseRedirect, QueryDict

from core.logs.forms import LogParsingForm, SearchLogForm
from core.logs.models import SiteLog


class LogParsingFormView(FormView):
    form_class = LogParsingForm
    template_name = 'logs/log_parse_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(redirect_to=self.success_url)


class SearchView(ListView):
    paginate_by = 1000
    template_name = 'logs/search_list.html'

    def get_queryset(self):
        qs = SiteLog.objects.all()
        if self.request.GET.get('site_name', None):
            qs = qs.filter(site_name=self.request.GET.get('site_name'))
        if self.request.GET.get('regex', None):
            qs = qs.filter(text__regex=r'^%s' % self.request.GET.get('regex'))
        if self.request.GET.get('text', None):
            qs = qs.filter(text__search=self.request.GET.get('text'))
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchLogForm()
        context['count'] = self.get_queryset().count()
        try:
            context['params'] = self.request.get_full_path().split('?')[1]
        except IndexError:
            context['params'] = ''
        return context
