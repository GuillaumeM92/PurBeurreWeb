from django.urls import path
from .views import FavoritesListView, favorite, rem_favorite

urlpatterns = [
    path("favorites", FavoritesListView.as_view(), name="favorites"),
    path("favorite", favorite, name="favorite"),
    path("rem_favorite", rem_favorite, name="rem_favorite"),
]
