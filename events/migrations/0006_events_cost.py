# Generated by Django 3.1.7 on 2021-04-03 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20210329_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]