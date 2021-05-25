from django.contrib import admin
from .models import *



admin.site.site_header = "Evolving Skills"
admin.site.site_title = "Evolving Skills"
admin.site.index_title = "Skills Learn"


admin.site.register(Profile)
admin.site.register(Course)
admin.site.register(CourseModule)
