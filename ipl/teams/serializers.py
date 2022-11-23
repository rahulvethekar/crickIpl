from rest_framework import serializers
from .models import Teams,Players,PlayerPersonalInformation


class TeamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teams
        fields = '__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Players
        fields = '__all__'

class PlayerPersonalInformationSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(many=True,read_only=True)
    class Meta:
        model = PlayerPersonalInformation
        fields = '__all__'
        