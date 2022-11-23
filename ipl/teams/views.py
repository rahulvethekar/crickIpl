from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Teams,PlayerPersonalInformation,Players
from .serializers import TeamsSerializer,PlayerSerializer,PlayerPersonalInformationSerializer

# Create your views here.

class TeamsApiView(APIView):

    def get(self,request):
        try:
            teams = Teams.objects.all()
            test_stored_procedure()
            team_serializer = TeamsSerializer(teams,many=True)
            return Response(team_serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(repr(e))


class PlayersApiView(APIView):

    def get(self,request):
        try:
            palyers = Players.objects.all()
            palyers_serializer = PlayerSerializer(palyers,many=True)
            return Response(palyers_serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(repr(e))

class PlayerPersonalInformationApiView(APIView):

    def get(self,request):
        try:
            personal_info = PlayerPersonalInformation.objects.all()
            qs = PlayerPersonalInformation.objects.filter(player_name__team='chennai super king')

            print(qs)
            personal_info_serializer = PlayerPersonalInformationSerializer(personal_info,many=True)
            return Response(personal_info_serializer.data,status=status.HTTP_200_OK)
        except Exception as e:
            return Response(repr(e))

from django.db import connection

def test_stored_procedure ():
    curser = connection.cursor()
    test = curser.execute('select * from teams_teams')
    print(curser.fetchall())
    out=curser.execute('call spTeams("Mumbai",@total)')
    result=curser.fetchall()
    print(out)
    print(result)

