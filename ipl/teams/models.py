from django.db import models

# Create your models here.


class Teams(models.Model):
    name = models.CharField(primary_key=True,max_length=50)
    titles = models.IntegerField()
    city = models.CharField(max_length=20)
    home_ground = models.CharField(max_length=50)


class Players(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    name = models.CharField(max_length=40,primary_key=True)


class PlayerPersonalInformation(models.Model):
    player_name = models.OneToOneField(Players,on_delete=models.CASCADE,primary_key=True)
    jersey_no = models.IntegerField(unique=True)
    age = models.IntegerField()
    role = models.CharField(max_length=40)
    batting_style = models.CharField(max_length=40)
    matches = models.IntegerField(default=0)
    runs = models.IntegerField(default=0)
    hundreds = models.IntegerField(default=0)
    fiftys = models.IntegerField()
    wickets = models.IntegerField(default=0)
    man_of_the_match = models.IntegerField(default=0)   #avg and highest score required
    profile_picture = models.ImageField(upload_to='player/images', blank=True)











    









