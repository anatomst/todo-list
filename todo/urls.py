from django.urls import path

from todo.views import ToDoList, TagsListView, TagsCreateView, TagsUpdateView, TagsDeleteView, TaskCreateView, \
    TaskUpdateView, TaskDeleteView, complete_button

urlpatterns = [
    path("", ToDoList.as_view(), name="homepage"),
    path("tags/", TagsListView.as_view(), name="tags"),
    path("tags/create/", TagsCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagsUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagsDeleteView.as_view(), name="tag-delete"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("<int:pk>/update", TaskUpdateView.as_view(), name="task-update"),
    path("<int:pk>/delete", TaskDeleteView.as_view(), name="task-delete"),
    path("change_status/<int:pk>/", complete_button, name="complete-button"),
]

app_name = "todo"
