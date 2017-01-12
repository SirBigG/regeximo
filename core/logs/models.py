from django.db import models

from django.utils.translation import ugettext_lazy as _


class SiteLog(models.Model):
    site_name = models.CharField(max_length=255, verbose_name=_("Site sign"))
    text = models.TextField(verbose_name=_("Log line content"))

    class Meta:
        verbose_name = _("Site log")
        verbose_name_plural = _("Site logs")

    def __str__(self):
        return self.text
