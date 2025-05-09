# Generated by Django 5.0.6 on 2024-07-11 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0006_donateur_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donateur',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 11, 13, 29, 45, 656048, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='donateur',
            name='decouverte',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donateur',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='donateur',
            name='message',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='donateur',
            name='nom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donateur',
            name='pays',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donateur',
            name='prenom',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='donateur',
            name='telephone',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
