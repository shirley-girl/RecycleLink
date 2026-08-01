from django.contrib import admin
from .models import WasteRequest
from .models import Company

# Register your models here.
admin.site.register(WasteRequest)
admin.site.register(Company)