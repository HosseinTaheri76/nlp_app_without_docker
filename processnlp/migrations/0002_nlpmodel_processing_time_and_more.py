# Generated by Django 4.0.2 on 2022-08-16 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processnlp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nlpmodel',
            name='processing_time',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=6, null=True, verbose_name='Processing time'),
        ),
        migrations.AlterField(
            model_name='nlpmodel',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Datetime created'),
        ),
        migrations.AlterField(
            model_name='nlpmodel',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Datetime modified'),
        ),
        migrations.AlterField(
            model_name='nlpmodel',
            name='nlp_model_num',
            field=models.CharField(choices=[('1', 'Number 1'), ('2', 'Number 2'), ('3', 'Number 3'), ('4', 'Number 4'), ('5', 'Number 5')], max_length=2, verbose_name='Nlp model number'),
        ),
    ]
