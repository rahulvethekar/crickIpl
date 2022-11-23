from django.urls import path
from .views import TeamsApiView,PlayerPersonalInformationApiView,PlayersApiView

urlpatterns = [
    path('teams/',TeamsApiView.as_view()),
    path('players/',PlayersApiView.as_view()),
    path('personal-info/',PlayerPersonalInformationApiView.as_view()),
]