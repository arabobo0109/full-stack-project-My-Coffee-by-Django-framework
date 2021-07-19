# Generated by Django 3.1.7 on 2021-03-23 13:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('to_active', models.BooleanField(default=True)),
                ('publish_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]