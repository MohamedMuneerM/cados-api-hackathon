from django.contrib import admin
from . import models

admin.AdminSite.site_title = "Cados Admin"
admin.AdminSite.site_header = "Cados Admin"
admin.AdminSite.site_url = "/docs"

admin.site.register(models.Advocate)
admin.site.register(models.Company)

