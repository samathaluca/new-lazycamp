# Generated by Django 3.0.6 on 2020-07-21 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campspots', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campspot',
            name='image_url',
        ),
        migrations.AddField(
            model_name='campspot',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='campspot',
            name='campspot_email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='campspot',
            name='local_eatery_and_shop',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='campspot',
            name='motorhome_service_point',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='campspot',
            name='nearest_toilet_and_shower',
            field=models.CharField(max_length=254),
        ),
        migrations.AlterField(
            model_name='campspot',
            name='public_transport_options',
            field=models.CharField(max_length=254),
        ),
    ]
