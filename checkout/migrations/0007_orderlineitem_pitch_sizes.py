# Generated by Django 3.0.6 on 2020-05-20 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_remove_orderlineitem_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='pitch_sizes',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
    ]