# Generated by Django 3.1.7 on 2021-03-28 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='payment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
    ]
