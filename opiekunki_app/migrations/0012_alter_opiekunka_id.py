# Generated by Django 5.0 on 2024-03-16 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opiekunki_app', '0011_alter_opinia_autor_alter_opinia_ocena'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opiekunka',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]