# Generated by Django 4.1.3 on 2022-12-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Author', models.CharField(max_length=255)),
                ('Isbn', models.CharField(max_length=255)),
                ('Publisher', models.CharField(max_length=255)),
            ],
        ),
    ]
