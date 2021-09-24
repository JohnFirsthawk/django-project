from django.contrib import admin

from .models import TaxesAdmin, UserAdmin, Users,Taxes

admin.site.register(Users, UserAdmin)
admin.site.register(Taxes, TaxesAdmin)
