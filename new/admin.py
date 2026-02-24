from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(Education)
admin.site.register(Skill)
admin.site.register(Training)
admin.site.register(Achievement)
admin.site.register(Project)
admin.site.register(Contact)
