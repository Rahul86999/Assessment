# Generated by Django 3.0.7 on 2020-07-06 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0003_question_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='options',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='assessment.Question'),
        ),
    ]
