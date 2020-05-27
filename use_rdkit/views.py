from django.shortcuts import render

# Create your views here.
import base64
from io import BytesIO
from rdkit import Chem
from rdkit.Chem import Draw
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from django_rdkit.config import config
from django_rdkit.models import *
from use_rdkit.models import *
from use_rdkit.serializers import CompoundSerializer


def get_mfp2_neighbors(smiles):
    value = MORGANBV_FP(Value(smiles))
    queryset = Compound.objects.filter(mfp2__tanimoto=value)
    queryset = queryset.annotate(smiles=MOL_TO_SMILES('molecule'))
    queryset = queryset.annotate(sml=TANIMOTO_SML('mfp2', value))
    queryset = queryset.order_by(TANIMOTO_DIST('mfp2', value))
    queryset = queryset.values_list('name', 'smiles', 'sml')
    return queryset


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10  # 默认两个
    max_page_size = 10  # 一页显示最大5个
    page_query_param = 'page'  # 页码


class StructuresimilarityView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        smiles = self.request.GET.get('pk1')
        similarity = self.request.GET.get('pk2')
        if smiles is not None:  # 如果参数不为空
            config.tanimoto_threshold = similarity
            l = {}
            i = 0
            for name, smiles, sml in get_mfp2_neighbors(eval(smiles))[:10]:
                i += 1
                m = Chem.MolFromSmiles(smiles)
                # print(m)
                image = Draw.MolToImage(m)
                # print(image)
                img_buffer = BytesIO()
                image.save(img_buffer, format='JPEG')
                byte_data = img_buffer.getvalue()
                base64_str = base64.b64encode(byte_data)
                # print(base64_str)
                a = {'name': name, 'smiles': smiles, 'sml': sml, 'image': base64_str}
                l[i] = a
            l = sorted(l.values(), key=lambda item: item['sml'], reverse=True)
            # print(l)
            # pg = MyPageNumberPagination()
            # # 执行filter()方法
            # queryset = Compound.objects.all()
            # pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            # serializer = CompoundSerializer(instance=pager_roles, many=True)
            return Response(l)
        else:
            pg = MyPageNumberPagination()
            # 执行filter()方法
            queryset = Compound.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = CompoundSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)


class SubstructuresimilarityView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        smiles = self.request.GET.get('pk')
        print(smiles)
        # similarity = self.request.GET.get('pk2')
        if smiles is not None:  # 如果参数不为空
            # config.tanimoto_threshold = similarity
            l = {}
            i = 0
            query = Compound.objects.filter(molecule__hassubstruct=eval(smiles))
            # print(query)
            for cmpd in query.annotate(smiles=MOL_TO_SMILES('molecule'))[:10]:
                i += 1
                m = Chem.MolFromSmiles(cmpd.smiles)
                # print(m)
                image = Draw.MolToImage(m)
                # print(image)
                img_buffer = BytesIO()
                image.save(img_buffer, format='JPEG')
                byte_data = img_buffer.getvalue()
                base64_str = base64.b64encode(byte_data)
                # print(base64_str)
                a = {'name': cmpd.name, 'smiles': cmpd.smiles, 'image': base64_str}
                l[i] = a
            l = sorted(l.values(), key=lambda item: item['name'], reverse=True)
            return Response(l)
        else:
            pg = MyPageNumberPagination()
            # 执行filter()方法
            queryset = Compound.objects.all()
            pager_roles = pg.paginate_queryset(queryset=queryset, request=request, view=self)
            serializer = CompoundSerializer(instance=pager_roles, many=True)
            return pg.get_paginated_response(serializer.data)
