from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _


class UserExternalData(models.Model):
    """
    Store external data from auth microservice user model
    """

    user_rel = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='user_external_data_rel',
                                    on_delete=models.CASCADE, verbose_name=_("User"), null=False, blank=False)
    external_id = models.IntegerField(null=False, verbose_name=_("External ID"))
    fullname = models.CharField(max_length=200, verbose_name=_("Full name"))

    class Meta:
        verbose_name = _("User's external data")
        verbose_name_plural = _('Users external data')

    def __str__(self):
        return _("External data ") + self.user_rel.username
