# Generated by Django 5.1 on 2024-09-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_alter_order_postcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='original_bag',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='stripe_pid',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
    ]
