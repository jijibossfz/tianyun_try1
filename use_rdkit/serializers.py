# coding=utf-8
from dynamic_rest.serializers import DynamicModelSerializer

from use_rdkit.models import Compound


class CompoundSerializer(DynamicModelSerializer):
    class Meta:
        model = Compound
        fields = ('name', 'molecule', 'torsionbv', 'mfp2',
                  'ffp2',)
