# Generated by Django 2.1.4 on 2020-03-31 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mindapp', '0014_auto_20200331_1037'),
    ]

    operations = [
        migrations.AddField(
            model_name='situation',
            name='ans',
            field=models.CharField(default='na', max_length=100),
        ),
    ]
