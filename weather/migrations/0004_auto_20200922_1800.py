# Generated by Django 2.2 on 2020-09-23 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0003_auto_20200919_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weather_type', models.CharField(max_length=50)),
                ('weather_image', models.CharField(max_length=3)),
                ('city_temperature', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='Temperature',
        ),
        migrations.DeleteModel(
            name='WeatherImage',
        ),
        migrations.DeleteModel(
            name='WeatherType',
        ),
    ]
