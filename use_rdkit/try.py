# coding=utf-8
import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tianyun_try1.settings")  # project_name 项目名称
django.setup()
path = '/home/jianping/fengzhe/NP_data/NP_db_local_easy.csv'
from rdkit import Chem
from use_rdkit.models import Compound

# def chembl(path, limit=None):
#     count = 0
#     with open(path, 'rt') as f:
#         next(f)  # skip header
#         for line in f:
#             b = line.split(',')
#             name = b[0]
#             smiles = b[1]
#             molecule = Chem.MolFromSmiles(smiles)
#             if molecule:
#                 yield name, molecule
#                 count += 1
#             if limit and count == limit:
#                 break
#
#
# for name, molecule in chembl(path, limit=None):
#     smiles = Chem.MolToSmiles(molecule)
#     test_molecule = Chem.MolFromSmiles(smiles)
#     if not test_molecule:
#         print('smiles-mol-smiles roundtrip issue:', name)
#     else:
#         Compound.objects.create(name=name, molecule=molecule)
#
# print(Compound.objects.count())

from django_rdkit.models import *

from use_rdkit.models import Compound

Compound.objects.update(torsionbv=TORSIONBV_FP('molecule'), mfp2=MORGANBV_FP('molecule'),
                        ffp2=FEATMORGANBV_FP('molecule'), )
