# Generated by Django 3.1.6 on 2021-02-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='polldata',
            name='option1_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='polldata',
            name='option2_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='polldata',
            name='option3_count',
            field=models.IntegerField(),
        ),
    ]
