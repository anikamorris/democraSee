# Generated by Django 3.0.2 on 2020-03-24 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0013_auto_20200324_0001'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='image_link',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
