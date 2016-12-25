from django.contrib import admin
from .models import Disease
from .models import Symptom
from .models import Treatment
from .models import Drug

admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(Treatment)
admin.site.register(Drug)
