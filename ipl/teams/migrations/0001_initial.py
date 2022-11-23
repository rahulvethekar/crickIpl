# Generated by Django 4.1.3 on 2022-11-12 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('titles', models.IntegerField()),
                ('city', models.CharField(max_length=20)),
                ('home_ground', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerPersonalInformation',
            fields=[
                ('player_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='teams.players')),
                ('jersey_no', models.IntegerField(unique=True)),
                ('age', models.IntegerField()),
                ('role', models.CharField(max_length=20)),
                ('batting_style', models.CharField(max_length=20)),
                ('matches', models.IntegerField(default=0)),
                ('runs', models.IntegerField(default=0)),
                ('hundreds', models.IntegerField(default=0)),
                ('fiftys', models.IntegerField()),
                ('wickets', models.IntegerField(default=0)),
                ('man_of_the_match', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='players',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.teams'),
        ),
    ]
