# Generated by Django 3.0.8 on 2020-07-20 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0003_auto_20200720_2135'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderinfo',
            old_name='pay_script',
            new_name='post_script',
        ),
        migrations.RenameField(
            model_name='shoppingcart',
            old_name='goods_num',
            new_name='nums',
        ),
    ]
