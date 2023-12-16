from django.urls import path
from . import views

app_name = "profiles"

urlpatterns = [
    path(
        "", views.index, name="profiles_index"
    ),  # Mise à jour de profiles_index en index
    path("<str:username>/", views.profile, name="profile"),
]
