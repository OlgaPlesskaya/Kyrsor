# Generated by Django 4.2.7 on 2024-01-15 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_vuz_1_distance_from_dormitory'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dormitory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.CharField(default='', max_length=255, verbose_name='Широта')),
                ('longitude', models.CharField(default='', max_length=255, verbose_name='Долгота')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.vuz_1', verbose_name='Название ВУЗа')),
            ],
        ),
    ]
