# Generated by Django 3.1 on 2020-08-18 12:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0010_questioncategory_updated_by'),
        ('project_admin', '0019_assigntest_test_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTestPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.IntegerField()),
                ('attempt', models.IntegerField()),
                ('assigned_test', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_admin.assigntest')),
                ('elearning_stu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_admin.individualstudents')),
                ('question', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='assessment.question')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='project_admin.student')),
            ],
        ),
    ]
