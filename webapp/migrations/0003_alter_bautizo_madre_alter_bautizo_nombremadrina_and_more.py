# Generated by Django 5.1.1 on 2024-09-11 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_alter_bautizo_fecha_bautizo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bautizo',
            name='madre',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='bautizo',
            name='nombremadrina',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='bautizo',
            name='nombrepadrino',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='bautizo',
            name='oficiante',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='bautizo',
            name='padre',
            field=models.CharField(max_length=80, null=True),
        ),
    ]
