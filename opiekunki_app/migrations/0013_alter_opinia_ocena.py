# Generated by Django 5.0 on 2024-03-16 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opiekunki_app', '0012_alter_opiekunka_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinia',
            name='ocena',
            field=models.IntegerField(),
        ),
    ]
