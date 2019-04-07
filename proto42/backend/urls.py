from django.urls import path, include
from rest_framework.routers import DefaultRouter

from backend import views

router = DefaultRouter()
router.register(r'artists', views.ArtistViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'albums', views.AlbumViewSet)
router.register(r'genres', views.GenreViewSet)

urlpatterns = [
        path('', include(router.urls)),
]
