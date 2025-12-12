from django.urls import path
from .views import list_users, create_user, update_user_partial, delete_user

urlpatterns = [
    path("", list_users, name="list_users"),                 # GET /users/
    path("create/", create_user, name="create_user"),        # POST /users/create/
    path("<int:pk>/", update_user_partial, name="update_user_partial"), # PATCH /users/<id>/
    path("<int:pk>/delete/", delete_user, name="delete_user"),         # DELETE /users/<id>/delete/
]