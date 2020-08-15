from django.contrib import admin
from .models import Audio, AudioSentence

from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(Audio,AudioSentence)
class AudiorecordAdmin(ImportExportModelAdmin):
    pass
