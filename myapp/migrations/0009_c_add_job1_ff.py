# Generated by Django 3.2 on 2022-10-25 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_regsave_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_add_job1',
            name='FF',
            field=models.FileField(null=True, upload_to='FileF/'),
        ),
    ]
