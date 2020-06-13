from django.urls import path
from .views import GetGroups, GetGroup, CreateGroup, UpdateGroup, DeleteGroup, RemoveUser

app_name = 'groups'
urlpatterns = [
    path('', GetGroups, name='list'),
    path('<int:id>', GetGroup, name='detail'),
    path('create/', CreateGroup.as_view(), name='create'),
    path('update/<int:id>', UpdateGroup.as_view(), name='update'),
    path('delete/<id>', DeleteGroup, name='delete'),
    path('delete_user/<int:id>', RemoveUser, name="remove_user")
]