from django.contrib import admin
from .models import Prepregnancy, Pregnancy, Parenting, Menu


admin.site.register(Parenting)
admin.site.register(Pregnancy)
admin.site.register(Prepregnancy)
admin.site.register(Menu)