# Generated by Django 4.2.9 on 2024-01-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todooapp', '0002_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1993-03-12'),
            preserve_default=False,
        ),
    ]