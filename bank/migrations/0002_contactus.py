# Generated by Django 3.2.3 on 2021-10-21 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('about', models.CharField(max_length=100)),
                ('concern', models.CharField(max_length=150)),
            ],
        ),
    ]
