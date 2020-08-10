from django.contrib import admin
from .models import WordSemantic, Label
from import_export.admin import ImportExportModelAdmin

# Register your models here.
@admin.register(WordSemantic,Label)
class WordSemanticAdmin(ImportExportModelAdmin):
    pass
