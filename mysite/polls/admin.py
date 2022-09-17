from django.contrib import admin

from .models import Question


# Changing an order in the form
# class QuestionAdmin(admin.ModelAdmin):
# fields = ['pub_date', 'question_text']


# Add fieldsets
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]


admin.site.register(Question, QuestionAdmin)
