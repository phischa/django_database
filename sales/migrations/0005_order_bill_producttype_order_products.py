# Generated by Django 5.1.4 on 2024-12-22 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_bill_product_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='bill',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, to='sales.bill'),
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=40)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='sales.ProductType', to='sales.product'),
        ),
    ]
