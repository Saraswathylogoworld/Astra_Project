# Generated by Django 3.2 on 2022-10-25 07:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_c_add_job1_ff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='c_add_job1',
            name='FF',
        ),
    ]