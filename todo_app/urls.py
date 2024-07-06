# todo-web-app/todo_app/urls.property
from django.urls import path
from todo_app import views


urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    # CRUD patterns for ToDoLists
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    # CRUD patterns for ToDoItems
    path("list/<int:list_id>/item/add/", views.ItemCreate.as_view(), name="item-add")
]
