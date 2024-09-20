# Generated by Django 5.0.6 on 2024-08-25 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='Rank',
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='rank',
            field=models.CharField(choices=[('pharmacy', 'PHARMACY'), ('DRIVERS', 'Drives'), ('company', 'COMAPNY')], default='pharmacy', max_length=50),
        ),
    ]
