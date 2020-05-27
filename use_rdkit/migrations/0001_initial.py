# Generated by Django 2.2.1 on 2019-08-29 04:42

from django.db import migrations, models
import django_rdkit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('molecule', django_rdkit.models.fields.MolField()),
            ],
        ),
    ]
