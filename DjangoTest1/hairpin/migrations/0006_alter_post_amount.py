# Generated by Django 4.2.7 on 2024-01-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hairpin', '0005_post_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
    ]
