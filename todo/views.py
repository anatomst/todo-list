from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Task, Tag


class ToDoList(generic.ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "todo/tasks_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:homepage")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:homepage")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "todo/task_confirm_delete.html"
    success_url = reverse_lazy("todo:homepage")


class TagsListView(generic.ListView):
    model = Tag
    template_name = "todo/tags_list.html"


class TagsCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags")


class TagsUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tags")


class TagsDeleteView(generic.DeleteView):
    model = Tag
    template_name = "todo/tag_confirm_delete.html"
    success_url = reverse_lazy("todo:tags")


def complete_button(request, pk):
    task = Task.objects.get(pk=pk)
    task.status = not task.status
    task.save()

    return HttpResponseRedirect(reverse("todo:homepage"))
