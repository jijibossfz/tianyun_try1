from django.db import models, migrations
from django_rdkit.operations import GiSTIndex


class Migration(migrations.Migration):

    dependencies = [
        ('use_rdkit', '0003_add_compound_fingerprint_fields'),
    ]

    operations = [
        GiSTIndex('Compound', 'mfp2')
    ]
