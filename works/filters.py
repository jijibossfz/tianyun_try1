# import django_filters
# from .models import *
#
#
# class ServerFilter(django_filters.rest_framework.FilterSet):
#     drug_name = django_filters.AllValuesFilter(field_name='drug_name', lookup_expr='icontains')
#     active_indications = django_filters.AllValuesFilter(field_name='active_indications', lookup_expr='icontains')
#     target_based_actions = django_filters.AllValuesFilter(field_name='target_based_actions', lookup_expr='icontains')
#     other_actions = django_filters.AllValuesFilter(field_name='other_actions', lookup_expr='icontains')
#
#     class Meta:
#         model = Extract
#         fields = ['drug_name', 'active_indications', 'target_based_actions', 'other_actions']
