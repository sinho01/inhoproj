# Generated by Django 3.1.4 on 2020-12-21 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0002_auto_20201211_0712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helloworld',
            name='date',
        ),
        migrations.AlterField(
            model_name='helloworld',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='helloworld',
            name='text',
            field=models.CharField(max_length=255),
        ),
    ]
