# Generated by Django 4.0.2 on 2022-08-16 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processnlp', '0002_nlpmodel_processing_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nlpmodel',
            name='processing_time',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=7, null=True, verbose_name='Processing time'),
        ),
    ]
