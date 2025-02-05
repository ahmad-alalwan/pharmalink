# Generated by Django 5.0.6 on 2024-08-25 22:36

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('name', models.CharField(max_length=25)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('locals', models.TextField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('account', models.IntegerField()),
                ('invoice', models.IntegerField(primary_key=True, serialize=False)),
                ('pharmacy', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pharmacies.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, unique=True)),
                ('quantity', models.IntegerField()),
                ('price', models.CharField(max_length=50)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('id_pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacies.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Register_medicien',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name_medicine', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('name_pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pharmacies.pharmacy')),
            ],
        ),
        migrations.CreateModel(
            name='Size_order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('id_name_medicien', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pharmacies.medicine')),
            ],
        ),
    ]
