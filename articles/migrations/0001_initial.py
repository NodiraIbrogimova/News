# Generated by Django 4.1.5 on 2023-01-31 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('publishedAt', models.DateTimeField()),
            ],
        ),
    ]
