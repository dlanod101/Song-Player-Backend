from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Song
from .serializers import SongSerializer

# Get All Songs
@api_view(['GET'])
def get_all_songs(request):
    songs = Song.objects.all()
    serializer = SongSerializer(songs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Get Specific Song
@api_view(['GET'])
def get_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    serializer = SongSerializer(song)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def create_song(request):
    print("Request data:", request.data)  # Debugging
    print("Request files:", request.FILES)  # Debugging

    serializer = SongSerializer(data=request.data)  

    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Song added", "data": serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response({"message": "Song not added. Bad request", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Update a Song (with file upload support)
@api_view(['PATCH'])
@parser_classes([MultiPartParser, FormParser])
def update_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    serializer = SongSerializer(song, data=request.data, partial=True)  
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Song updated", "data": serializer.data}, status=status.HTTP_200_OK)
    return Response({"message": "Bad request", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

# Delete a Song
@api_view(['DELETE'])
def delete_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    song.delete()
    return Response({"message": "Song Deleted"}, status=status.HTTP_200_OK)

# Delete Multiple Songs
@api_view(['DELETE'])
def delete_multiple_songs(request):
    song_ids = request.data.get("marked_songs", [])
    if not song_ids:
        return Response({"message": "No songs provided"}, status=status.HTTP_400_BAD_REQUEST)
    
    deleted_count, _ = Song.objects.filter(id__in=song_ids).delete()
    if deleted_count == 0:
        return Response({"message": "Song(s) not found."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "Songs Deleted"}, status=status.HTTP_200_OK)

# Delete All Songs
@api_view(['DELETE'])
def delete_all_songs(request):
    deleted_count, _ = Song.objects.all().delete()
    if deleted_count == 0:
        return Response({"message": "No songs found."}, status=status.HTTP_404_NOT_FOUND)

    return Response({"message": "All Songs have been Deleted"}, status=status.HTTP_200_OK)
