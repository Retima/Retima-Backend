# Generated by Django 4.2.7 on 2024-01-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='tid',
            field=models.CharField(db_index=True, default='T92709JGP', max_length=10, unique=True),
        ),
    ]