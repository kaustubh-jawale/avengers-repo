# Generated by Django 3.2.6 on 2021-08-26 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interview', '0005_rename_hr_human_resources'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_first_name', models.CharField(max_length=50, null='False')),
                ('emp_last_name', models.CharField(max_length=50, null='False')),
                ('emp_Email', models.EmailField(default='', max_length=50)),
                ('emp_Skill', models.CharField(default='', max_length=50)),
                ('emp_from_exp', models.CharField(default='', max_length=50)),
                ('emp_to_exp', models.CharField(default='', max_length=50)),
                ('emp_date', models.CharField(default='', max_length=50)),
                ('emp_start_time', models.CharField(max_length=50)),
                ('emp_end_time', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
