from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

    
class ProductConfig(AppConfig):
    name = 'src.product'
    verbose_name = _('Product')
