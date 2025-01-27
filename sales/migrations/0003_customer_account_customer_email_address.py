# Generated by Django 5.1.4 on 2024-12-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_customer_newsletter_abo'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='account',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='email_address',
            field=models.EmailField(blank=True, default='', max_length=30),
        ),
    ]
