from django.urls import path
from .views import get_users, create_user, update_user, delete_user

urlpatterns = [
    path('list/', get_users),
    path('create/', create_user),
    path('update/<int:id>/', update_user),
    path('delete/<int:id>/', delete_user),
]