from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Question, Choice

# Register your models here.

#admin.site.register(Question)
"""class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']"""

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    AdminSite.site_header = 'polls admin'



admin.site.register(Question,QuestionAdmin)
#admin.site.register(Choice)