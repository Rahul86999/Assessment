# Generated by Django 3.0.7 on 2020-07-08 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('assessment', '0008_auto_20200707_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='questioncategory',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cat_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='QuestionHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assessment.Test')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]