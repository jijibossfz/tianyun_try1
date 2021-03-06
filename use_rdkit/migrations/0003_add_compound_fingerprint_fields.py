# Generated by Django 2.2.1 on 2019-08-29 06:10

from django.db import migrations
import django_rdkit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('use_rdkit', '0002_create_compound_molecule_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound',
            name='ffp2',
            field=django_rdkit.models.fields.BfpField(null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='mfp2',
            field=django_rdkit.models.fields.BfpField(null=True),
        ),
        migrations.AddField(
            model_name='compound',
            name='torsionbv',
            field=django_rdkit.models.fields.BfpField(null=True),
        ),
    ]
