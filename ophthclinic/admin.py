from django.contrib import admin
from .models import *


admin.site.register(User)
admin.site.register(client)
admin.site.register(dosageforms)
admin.site.register(medications)
admin.site.register(thewholemed)
admin.site.register(prescription)
admin.site.register(info)