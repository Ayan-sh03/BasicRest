from base.views import UrlView,TodoView,TodoAll

from django.urls import path,include


urlpatterns =[
    path('url/',UrlView.as_view()),
    path('todo/', TodoAll.as_view(), name='all_todos'),
    path('todo/<int:t_id>/',TodoView.as_view(),name='get_todo_by_id'),
]