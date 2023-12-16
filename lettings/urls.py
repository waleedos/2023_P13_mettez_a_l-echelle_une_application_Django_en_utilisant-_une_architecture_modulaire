from django.urls import path
from . import views

app_name = "lettings"

urlpatterns = [
    path("", views.index, name="lettings_index"),
    # Mise à jour de lettings_index en index
    path("<int:letting_id>/", views.letting, name="letting"),
]
