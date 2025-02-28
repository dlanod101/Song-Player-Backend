from django.urls import path
from .views import (
    get_all_songs, get_song, create_song, update_song, 
    delete_song, delete_multiple_songs, delete_all_songs
)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('list/', get_all_songs, name='list_songs'),
    path('get/<int:song_id>/', get_song, name='get_song'),
    path('create/', create_song, name='create_song'),
    path('update/<int:song_id>/', update_song, name='update_song'),
    path('delete/<int:song_id>/', delete_song, name='delete_song'),
    path('songs/', delete_multiple_songs, name='delete_multiple_songs'),
    path('all_songs/', delete_all_songs, name='delete_all_songs'),
]

# ✅ Add this to serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
