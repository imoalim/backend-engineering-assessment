from django.contrib import admin
from .models import Quiz, Question, Answer, Participant


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionInline(admin.TabularInline):
    model = Question


class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Participant)
