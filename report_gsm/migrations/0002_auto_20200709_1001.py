# Generated by Django 3.0.8 on 2020-07-09 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report_gsm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LimitTipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_limit_type', models.CharField(max_length=15, verbose_name='Тип лимита')),
            ],
        ),
        migrations.CreateModel(
            name='Nomenclature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_nomenclature', models.CharField(max_length=15, verbose_name='Номенклатура')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='pin',
            field=models.IntegerField(default=0, verbose_name='Пин-код'),
        ),
        migrations.AddField(
            model_name='card',
            name='limit_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report_gsm.LimitTipe'),
        ),
        migrations.AddField(
            model_name='card',
            name='nomenclature',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report_gsm.Nomenclature'),
        ),
    ]
