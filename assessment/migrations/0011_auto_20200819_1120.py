# Generated by Django 3.1 on 2020-08-19 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0010_questioncategory_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='options',
            name='option1',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='options',
            name='option2',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='options',
            name='option3',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='options',
            name='option4',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
