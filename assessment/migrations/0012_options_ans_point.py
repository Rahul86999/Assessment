# Generated by Django 3.1 on 2020-08-20 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0011_auto_20200819_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='ans_point',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
    ]