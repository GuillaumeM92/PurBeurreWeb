from django.urls import path
from .views import FavoritesListView, favorite

urlpatterns = [
    path("favorites/", FavoritesListView.as_view(), name="favorites"),
    path("favorite/", favorite, name="favorite"),
]
