from django.forms import ModelForm, TextInput, Textarea, Form, BooleanField, NumberInput, NullBooleanSelect
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import modelformset_factory
from .models import Question, Option, Test, TrueFalse, FreeText
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'description']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-test',
                'placeholder': 'Title',
                'required': 'true',
            }),
            'description': Textarea(attrs={
                'class': 'form-test',
                'placeholder': 'Please about Test',
                'rows': 7,
            })
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }


class QuestionForm(ModelForm):
    class Meta:
        model = Question

        fields = ['text', 'ranking']

        widgets = {
            'text': CKEditorUploadingWidget(attrs={
                'class': 'form-question',
                'rows': 4, 'required': 'true',
            }),
            'ranking': NumberInput(attrs={
                'class': 'form-question-rank',
                'placeholder': 1,
                'required': 'true',
            })
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }


class OptionForm(ModelForm):
    class Meta:
        model = Option

        fields = ['answer', 'is_correct']

        widgets = {
            'answer': CKEditorUploadingWidget(attrs={
                'class': 'form-option',
                'rows':4,
                'required': 'true',
            }),
            'is_correct': NullBooleanSelect(attrs={
                'class':'form-correct',
                'required':'true'
            })
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }


class TrueFalseForm(ModelForm):
    class Meta:
        model = TrueFalse

        fields = ['true', 'false']

        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }


class DeleteForm(Form):
    confirmation = BooleanField(label='Confirm Deletion', required=True)


class FreeTextForm(ModelForm):
    class Meta:
        model = FreeText

        fields = ['freetext']

        widgets = {
            'freetext': CKEditorUploadingWidget(attrs={
                'class': 'form-freetext',
                'rows':4,
                'required': 'true',
            })
        }

        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }


OptionFormSet = modelformset_factory(Option, OptionForm, fields=('answer', 'is_correct'), extra=3)
TrueFalseFormSet = modelformset_factory(TrueFalse, TrueFalseForm, fields=('true', 'false'), extra=1)
FreeTextFormSet = modelformset_factory(FreeText, FreeTextForm, fields=('freetext',), extra=1)
