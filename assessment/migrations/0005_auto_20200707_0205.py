# Generated by Django 3.0.7 on 2020-07-06 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0004_auto_20200706_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='test_name',
            new_name='package',
        ),
        migrations.AddField(
            model_name='test',
            name='quater',
            field=models.CharField(default='Quater1', max_length=50),
        ),
        migrations.AddField(
            model_name='test',
            name='subject_name',
            field=models.CharField(default='Package', max_length=90),
        ),
        migrations.AddField(
            model_name='test',
            name='test_year',
            field=models.IntegerField(default=2020),
        ),
    ]
