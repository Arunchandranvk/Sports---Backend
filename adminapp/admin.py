from django.contrib import admin
from adminapp.models import *



admin.site.register(CustomUser)
admin.site.register(Event)
admin.site.register(StudentProfile)
admin.site.register(Sponsorship)
admin.site.register(Winner)