# Generated by Django 3.0.8 on 2020-07-20 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0002_auto_20200720_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderinfo',
            options={'verbose_name': '订单', 'verbose_name_plural': '订单'},
        ),
    ]
