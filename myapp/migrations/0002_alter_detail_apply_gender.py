# Generated by Django 3.2 on 2022-10-05 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail_apply',
            name='gender',
            field=models.CharField(max_length=200, null=True),
        ),
    ]