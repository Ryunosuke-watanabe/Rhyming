# Generated by Django 3.1.7 on 2021-02-27 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputRhyme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(null=True)),
            ],
            options={
                'db_table': 'input_rhyme',
            },
        ),
    ]
