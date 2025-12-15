from django.urls import path
from .views import users_list_create, update_user_partial, delete_user

urlpatterns = [
    path("", users_list_create, name="users_list_create"),   # GET + POST
    path("<int:pk>/", update_user_partial),
    path("<int:pk>/delete/", delete_user),
]