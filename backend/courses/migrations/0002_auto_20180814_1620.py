# Generated by Django 2.1 on 2018-08-14 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='course',
            name='reward_percent',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]
