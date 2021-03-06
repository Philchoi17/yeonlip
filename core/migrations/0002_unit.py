# Generated by Django 3.0.6 on 2020-05-13 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.FloatField()),
                ('block_name', models.CharField(max_length=255)),
                ('floor_number', models.IntegerField()),
                ('floor_type_code', models.IntegerField()),
                ('floor_type_name', models.CharField(max_length=255)),
                ('unit_name', models.CharField(max_length=255)),
                ('est_price_m2', models.IntegerField()),
                ('est_price', models.IntegerField()),
                ('yeonlip_building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Yeonlip')),
            ],
        ),
    ]
