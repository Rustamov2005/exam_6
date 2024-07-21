# Generated by Django 5.0.7 on 2024-07-21 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('like', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('userid', models.ManyToManyField(to='home.users')),
            ],
        ),
    ]