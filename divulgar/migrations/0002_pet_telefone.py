# Generated by Django 4.1.5 on 2023-01-12 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divulgar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='telefone',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
