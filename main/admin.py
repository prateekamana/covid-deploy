from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries, Blog

admin.site.register(Tutorial)
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Blog)

# Register your models here.
