# Generated by Django 3.0.7 on 2020-07-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_admin', '0013_authorityaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='authorityaccount',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]