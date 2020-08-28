# Generated by Django 3.0.9 on 2020-08-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugtrackerapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('inpr', 'In Progress'), ('done', 'Done'), ('inv', 'Invalid')], default='new', max_length=4),
        ),
    ]