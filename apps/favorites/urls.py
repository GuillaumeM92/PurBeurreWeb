from django.urls import path
from . import views
from .views import FavoritesListView

urlpatterns = [
    path("favorites/", FavoritesListView.as_view(), name="favorites"),
]
