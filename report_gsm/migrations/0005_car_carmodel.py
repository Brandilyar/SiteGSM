# Generated by Django 3.0.8 on 2020-07-09 08:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report_gsm', '0004_auto_20200709_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_model', models.CharField(max_length=30, verbose_name='Модель ТС')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('government_number', models.CharField(max_length=10, verbose_name='Государтсвенный номер')),
                ('car_type', models.CharField(max_length=30, verbose_name='Тип ТС')),
                ('year_of_issue', models.CharField(max_length=50, verbose_name='Год')),
                ('vin', models.CharField(max_length=50, verbose_name='Vin номер')),
                ('color', models.CharField(max_length=50, verbose_name='Цвет')),
                ('power', models.CharField(max_length=50, verbose_name='Мощность')),
                ('car_model', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report_gsm.CarModel')),
                ('car_nomenclature', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report_gsm.Nomenclature')),
            ],
        ),
    ]