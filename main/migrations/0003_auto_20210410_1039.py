# Generated by Django 3.2 on 2021-04-10 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20210410_0856'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='switch',
            name='switch_state1',
        ),
        migrations.AddField(
            model_name='switch',
            name='switch_state',
            field=models.CharField(default='Some string', max_length=100),
        ),
    ]
