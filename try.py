# coding=utf-8
import io

from PIL import Image
from rdkit import Chem
from rdkit.Chem import Draw

smi = 'CCCc1nn(C)c2C(=O)NC(=Nc12)c3cc(ccc3OCC)S(=O)(=O)N4CCN(C)CC4'
m = Chem.MolFromSmiles(smi)
Draw.MolToImageFile(m,'mol.jpg')


import base64
from io import BytesIO

# img_buffer = BytesIO()
# a.save(img_buffer, format='JPEG')
# byte_data = img_buffer.getvalue()
# base64_str = base64.b64encode(byte_data)
# print(base64_str)
# 图片转字节
with open('mol.jpg', 'rb') as fp:
    tu = base64.b64encode(fp.read())
    print(tu)
