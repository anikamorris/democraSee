# Generated by Django 3.0.2 on 2020-03-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0004_candidate_foreign_policy'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='unique',
            field=models.TextField(null=True, verbose_name='what makes this candidate unique'),
        ),
    ]