# Generated by Django 4.0.2 on 2022-08-15 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NlpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_text', models.TextField(verbose_name='Original text')),
                ('nlp_model_num', models.CharField(choices=[('1', 'Number 1'), ('2', 'Number 2'), ('3', 'Number 3'), ('4', 'Number 4'), ('5', 'Number 5')], max_length=2, verbose_name='Nlp Model Number')),
                ('summary', models.TextField(blank=True, null=True, verbose_name='Summary')),
                ('datetime_created', models.DateTimeField(auto_now_add=True, verbose_name='Datetime Created')),
                ('datetime_modified', models.DateTimeField(auto_now=True, verbose_name='Datetime Modified')),
            ],
            options={
                'verbose_name': 'Nlp model',
                'verbose_name_plural': 'Nlp models',
                'ordering': ('-datetime_created',),
            },
        ),
    ]
