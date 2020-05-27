from django.db import models, migrations
from django_rdkit.operations import GiSTIndex


class Migration(migrations.Migration):
    dependencies = [
        ('use_rdkit', '0001_initial'),
    ]

    operations = [
        GiSTIndex('Compound', 'molecule')
    ]
