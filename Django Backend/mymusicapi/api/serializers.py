from rest_framework import serializers
from .models import Song  # ✅ Import the model instead

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'
