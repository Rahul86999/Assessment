# Generated by Django 3.0.7 on 2020-07-13 08:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Authority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority_name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('address', models.TextField()),
                ('person_incharge', models.CharField(max_length=50)),
                ('scool_auth', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='authority', to='project_admin.Authority')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='school_pro', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
