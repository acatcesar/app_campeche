from django.contrib import admin
from .models import Hospede, Apartamento, Usuario
from django.contrib.auth.admin import UserAdmin

admin.site.register(Hospede)
admin.site.register(Apartamento)
admin.site.register(Usuario, UserAdmin)
