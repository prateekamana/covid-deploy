from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries

admin.site.register(Tutorial)
admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)

# Register your models here.
