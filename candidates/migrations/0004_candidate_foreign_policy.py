# Generated by Django 3.0.2 on 2020-03-05 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_auto_20200305_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='foreign_policy',
            field=models.TextField(null=True),
        ),
    ]