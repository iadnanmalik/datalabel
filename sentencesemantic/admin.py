from django.contrib import admin
from .models import SentenceSemantic, Label
from import_export.admin import ImportExportModelAdmin

@admin.register(SentenceSemantic,Label)
class SentencesemanticAdmin(ImportExportModelAdmin):
    pass
