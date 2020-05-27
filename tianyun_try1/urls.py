from __future__ import unicode_literals
from rest_framework_jwt.views import obtain_jwt_token

from use_rdkit.views import StructuresimilarityView, SubstructuresimilarityView
from users.views import UserinfoViewset, PasswordresetViewset, UserRegViewset
# from django.urls import path, include
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import refresh_jwt_token
from rest_framework_jwt.views import verify_jwt_token
from works.views import NpDbLocalViewSet, NPidinotherdatabaseViewSet, NPenglishnamecasViewSet, NPderivativeassayViewSet, \
    NPderivativeidViewSet, NPDtargetinfoViewSet, NPassayViewSet, InfoClinical2View, PhaseDistributionView, \
    TargetDistributionView, InfoDrugViewSet, InfoClinicalViewSet, FDAPatentView, FDAdrugOrangeBookView, FDAdrugView, \
    InactiveIngredientSearchView, GenericDrugDataView, ChemicalIndexView, ClinicalDataBigViewSet

router = DefaultRouter()

# router.register(r'YNpDbLocal', NpDbLocalViewSet)
# router.register(r'NPidinotherdatabase', NPidinotherdatabaseViewSet)
# router.register(r'NPenglishnamecas', NPenglishnamecasViewSet)
# router.register(r'NPderivativeassay', NPderivativeassayViewSet)
# router.register(r'NPderivativeid', NPderivativeidViewSet)
# router.register(r'NPDtargetinfo', NPDtargetinfoViewSet)
# router.register(r'NPassay', NPassayViewSet)
router.register(r'InfoDrug', InfoDrugViewSet)
router.register(r'InfoClinical', InfoClinicalViewSet)
# router.register(r'registers', UserRegViewset, base_name='用户注册')
# router.register(r'users', UserinfoViewset, base_name="user")
# router.register(r'passwordreset', PasswordresetViewset, base_name='passwordreset')
router.register(r'ClinicalDataBig', ClinicalDataBigViewSet)


urlpatterns = [
    url('', include(router.urls)),
    # url(r'^Structuresimilarity/$', StructuresimilarityView.as_view()),
    # url(r'^Substructuresimilarity/$', SubstructuresimilarityView.as_view()),
    url('admin/', admin.site.urls),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^InfoClinical2/$', InfoClinical2View.as_view()),
    url(r'^PhaseDistribution/$', PhaseDistributionView.as_view()),
    url(r'^TargetDistribution/$', TargetDistributionView.as_view()),
    url(r'^FDAPatent/$', FDAPatentView.as_view()),
    url(r'^FDAdrugOrangeBook/$', FDAdrugOrangeBookView.as_view()),
    url(r'^FDAdrug/$', FDAdrugView.as_view()),
    url(r'^InactiveIngredientSearch/$', InactiveIngredientSearchView.as_view()),
    url(r'^GenericDrugData/$', GenericDrugDataView.as_view()),
    url(r'^ChemicalIndex/$', ChemicalIndexView.as_view()),
]




