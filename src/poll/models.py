from django.db import models
from django.utils.translation import ugettext_lazy as _


class Poll(models.Model):
    question = models.TextField()
    option_one = models.CharField(max_length=30)
    option_two = models.CharField(max_length=30)
    option_three = models.CharField(max_length=30)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)
    option_three_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count + self.option_three_count

    class Meta:
        verbose_name = _("Санал асуулга")
        verbose_name_plural = _("Санал асуулга")
        ordering = ['question']
