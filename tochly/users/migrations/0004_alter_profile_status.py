# Generated by Django 4.2.7 on 2023-12-30 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, choices=[('', ''), ('In a Meeting', 'meeting'), ('Commuting', 'commuting'), ('Working Remotely', 'remote'), ('Sick', 'sick'), ('In Leave', 'leave')], default='', max_length=20, null=True),
        ),
    ]