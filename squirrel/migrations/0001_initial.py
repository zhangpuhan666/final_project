# Generated by Django 3.0.7 on 2021-04-13 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField(help_text='Latitude')),
                ('Longitude', models.FloatField(help_text='Longitude')),
                ('Unique_Squirrel_Id', models.CharField(help_text='The unique squirrel ID', max_length=80)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], help_text='AM or PM?', max_length=2)),
                ('Date', models.DateField(blank=True, help_text='what is the date')),
                ('Age', models.CharField(blank=True, choices=[('ADULT', 'ADULT'), ('JUVENILE', 'JUVENILE'), ('UNKNOWN', '?')], help_text='Age', max_length=80)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnamon', 'Cinnamon')], help_text='what is the fur color', max_length=10)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], help_text='Location', max_length=80)),
                ('Specific_Location', models.CharField(blank=True, help_text='specific location', max_length=80)),
                ('Running', models.BooleanField(blank=True, help_text='Running')),
                ('Chasing', models.BooleanField(blank=True, help_text='Chasing')),
                ('Climbing', models.BooleanField(blank=True, help_text='Climbing')),
                ('Eating', models.BooleanField(blank=True, help_text='Eating')),
                ('Foraging', models.BooleanField(blank=True, help_text='Foraging')),
                ('Other_Activities', models.CharField(blank=True, help_text='Other Activities', max_length=80)),
                ('Kuks', models.BooleanField(blank=True, help_text='Kuks')),
                ('Quaas', models.BooleanField(blank=True, help_text='Quaas')),
                ('Moans', models.BooleanField(blank=True, help_text='Moans')),
                ('Tail_Flags', models.BooleanField(blank=True, help_text='Tail_Flags')),
                ('Tail_Twitches', models.BooleanField(blank=True, help_text='Tail_Twitches')),
                ('Approaches', models.BooleanField(blank=True, help_text='Approaches')),
                ('Indifferent', models.BooleanField(blank=True, help_text='Indifferent')),
                ('Runs_From', models.BooleanField(blank=True, help_text='Runs_From')),
            ],
        ),
    ]
