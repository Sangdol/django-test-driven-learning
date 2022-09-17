from django.contrib import admin

from .models import Question, Choice


# TabularInline looks more compact than StackedInline
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


# Changing an order in the form
# class QuestionAdmin(admin.ModelAdmin):
# fields = ['pub_date', 'question_text']


# Add fieldsets
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ['question_text', 'pub_date', 'was_published_recently']
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# This is possible but adding ChoiceInline is better to manage choices.
# admin.site.register(Choice)
