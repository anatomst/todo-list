from django import forms

from todo.models import Tag, Task


class DateTime(forms.DateTimeInput):
    input_type = "datetime-local"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
                                          widget=forms.CheckboxSelectMultiple,
                                          required=False)

    deadline = forms.DateTimeField(widget=DateTime)

    class Meta:
        model = Task
        fields = "__all__"

