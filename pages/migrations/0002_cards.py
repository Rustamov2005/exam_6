# Generated by Django 5.0.7 on 2024-07-21 18:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_comments'),
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('total', models.IntegerField()),
                ('shipping', models.BooleanField(default=False)),
                ('cardnumber', models.CharField(max_length=16)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.users')),
            ],
        ),
    ]