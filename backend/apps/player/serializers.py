from rest_framework import serializers
from .models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ['id','username','created_at']
        read_only_fields = ['id', 'created_at']