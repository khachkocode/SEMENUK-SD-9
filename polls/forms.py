from django import forms
from django.forms import inlineformset_factory

from .models import Question
from .models import Choice


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']


ChoiceFormSet = inlineformset_factory(
    Question,
    Choice,
    form=ChoiceForm,
    extra=4,
    can_delete=True
)
