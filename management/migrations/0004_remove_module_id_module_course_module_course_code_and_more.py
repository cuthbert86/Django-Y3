# Generated by Django 4.2.17 on 2024-12-28 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_rename_todaysdate_registration_registration_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='module',
            name='id',
        ),
        migrations.AddField(
            model_name='module',
            name='Course',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='module',
            name='Course_Code',
            field=models.CharField(default='0000', max_length=50),
        ),
        migrations.AddField(
            model_name='module',
            name='Description',
            field=models.TextField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='module',
            name='avalaible',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes'),
        ),
        migrations.AddField(
            model_name='module',
            name='category',
            field=models.BooleanField(choices=[('compulsary', 'compulsary'), ('voluntary', 'voluntary')], default='voluntary'),
        ),
        migrations.AddField(
            model_name='module',
            name='credits',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='module',
            name='name',
            field=models.CharField(default='', max_length=100, primary_key=True, serialize=False),
        ),
    ]
