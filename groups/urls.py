from django.urls import path
from .views import GetGroups, GetGroup, CreateGroup, UpdateGroup, DeleteUser

app_name = 'groups'
urlpatterns = [
    path('', GetGroups, name='list'),
    path('<int:id>', GetGroup, name='detail'),
    path('create/', CreateGroup.as_view(), name='create'),
    path('update/<int:id>', UpdateGroup.as_view(), name='update'),
    path('delete_user/<int:id>', DeleteUser, name='delete_user')
]