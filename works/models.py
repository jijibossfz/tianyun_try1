# encoding:utf-8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class InfoDrug(models.Model):
    drug_name = models.TextField(db_column='Drug_Name', blank=True, null=True)  # Field name made lowercase.
    other_drug_names = models.TextField(db_column='Other_Drug_Names', blank=True,
                                        null=True)  # Field name made lowercase.
    originator_company = models.TextField(db_column='Originator_Company', blank=True,
                                          null=True)  # Field name made lowercase.
    active_companies = models.TextField(db_column='Active_Companies', blank=True,
                                        null=True)  # Field name made lowercase.
    active_indications = models.TextField(db_column='Active_Indications', blank=True,
                                          null=True)  # Field name made lowercase.
    target_based_actions = models.TextField(db_column='Target_based_Actions', blank=True,
                                            null=True)  # Field name made lowercase.
    highest_status = models.TextField(db_column='Highest_Status', blank=True, null=True)  # Field name made lowercase.
    technologies = models.TextField(db_column='Technologies', blank=True, null=True)  # Field name made lowercase.
    total_reported_sales_2014_usd_m = models.TextField(db_column='Total_Reported_Sales_2014_USD_M', blank=True,
                                                       null=True)  # Field name made lowercase.
    total_forecast_sales_2020_usd_m = models.TextField(db_column='Total_Forecast_Sales_2020_USD_M', blank=True,
                                                       null=True)  # Field name made lowercase.
    inactive_companies = models.TextField(db_column='Inactive_Companies', blank=True,
                                          null=True)  # Field name made lowercase.
    inactive_indications = models.TextField(db_column='Inactive_Indications', blank=True,
                                            null=True)  # Field name made lowercase.
    other_actions = models.TextField(db_column='Other_Actions', blank=True, null=True)  # Field name made lowercase.
    last_change_date = models.TextField(db_column='Last_Change_Date', blank=True,
                                        null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'info_drug'


class TargetDistribution(models.Model):
    active_indications = models.TextField(db_column='Active_Indications', blank=True,
                                          null=True)  # Field name made lowercase.
    target_based_actions = models.TextField(db_column='Target_based_Actions', blank=True,
                                            null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'info_TargetDistribution'


class InfoClinical(models.Model):
    title = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    condation = models.TextField(blank=True, null=True)
    intervention = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'info_clinical'


class PhaseDistribution(models.Model):
    phase = models.TextField(blank=True, null=True)
    condation = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'info_PhaseDistribution'


class InfoClinical2(models.Model):
    title = models.TextField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    condation = models.TextField(blank=True, null=True)
    intervention = models.TextField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'info_clinical2'


class NPidinotherdatabase(models.Model):
    database_id = models.CharField(max_length=255, blank=True, null=True)
    standard_inchi_key = models.CharField(max_length=255, blank=True, null=True)
    chembl_id = models.CharField(max_length=255, blank=True, null=True)
    sn_id = models.CharField(max_length=255, blank=True, null=True)
    pubchem_cid = models.CharField(max_length=255, blank=True, null=True)
    np_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'np_id_in_other_database'
        ordering = ['database_id']


class NPenglishnamecas(models.Model):
    database_id = models.CharField(max_length=255, blank=True, null=True)
    iupac_name = models.TextField(blank=True, null=True)
    pref_name = models.TextField(blank=True, null=True)
    cas = models.TextField(blank=True, null=True)

    # idinother = models.OneToOneField(NPidinotherdatabase, on_delete=models.CASCADE, to_field='database_id', null=True,
    #                                  blank=True)

    class Meta:
        db_table = 'np_english_name_cas'
        ordering = ['database_id']


class NpDbLocal(models.Model):
    database_id = models.CharField(max_length=255, blank=True, null=True)
    formula = models.CharField(max_length=255, blank=True, null=True)
    standard_inchi = models.TextField(blank=True, null=True)
    standard_inchi_key = models.CharField(max_length=255, blank=True, null=True)
    canonical_smiles = models.TextField(blank=True, null=True)
    slogp = models.FloatField(db_column='SlogP', blank=True, null=True)  # Field name made lowercase.
    tpsa = models.FloatField(db_column='TPSA', blank=True, null=True)  # Field name made lowercase.
    amw = models.FloatField(db_column='AMW', blank=True, null=True)  # Field name made lowercase.
    numrotatablebonds = models.SmallIntegerField(db_column='NumRotatableBonds', blank=True,
                                                 null=True)  # Field name made lowercase.
    numhbd = models.SmallIntegerField(db_column='NumHBD', blank=True, null=True)  # Field name made lowercase.
    numhba = models.SmallIntegerField(db_column='NumHBA', blank=True, null=True)  # Field name made lowercase.
    numheavyatoms = models.SmallIntegerField(db_column='NumHeavyAtoms', blank=True,
                                             null=True)  # Field name made lowercase.
    numrings = models.SmallIntegerField(db_column='NumRings', blank=True, null=True)  # Field name made lowercase.

    # englishname = models.OneToOneField(NPenglishnamecas, on_delete=models.CASCADE, to_field='database_id', null=True,
    #                                    blank=True)

    class Meta:
        db_table = 'np_db_local'
        ordering = ['database_id']


class NPderivativeid(models.Model):
    database_id = models.CharField(max_length=255, blank=True, null=True)
    derivative_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'np_derivative_id'


class NPderivativeassay(models.Model):
    derivative_id = models.CharField(max_length=255, blank=True, null=True)
    molecule_chembl_id = models.CharField(max_length=255, blank=True, null=True)
    target_id = models.CharField(max_length=255, blank=True, null=True)
    activity_type = models.CharField(max_length=255, blank=True, null=True)
    activity_relation = models.CharField(max_length=255, blank=True, null=True)
    activity_value = models.CharField(max_length=255, blank=True, null=True)
    activity_units = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    data_source_db = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'np_derivative_assay'


class NPDtargetinfo(models.Model):
    target_id = models.CharField(max_length=255, blank=True, null=True)
    target_type = models.CharField(max_length=255, blank=True, null=True)
    pref_name = models.CharField(max_length=255, blank=True, null=True)
    organism = models.CharField(max_length=255, blank=True, null=True)
    target_chembl_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'np_target_info'


class NPassay(models.Model):
    database_id = models.CharField(max_length=255, blank=True, null=True)
    target_id = models.CharField(max_length=255, blank=True, null=True)
    activity_type_sub = models.CharField(max_length=255, blank=True, null=True)
    activity_relation = models.CharField(max_length=255, blank=True, null=True)
    activity_value = models.CharField(max_length=255, blank=True, null=True)
    activity_units = models.CharField(max_length=255, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    reference_type = models.CharField(max_length=255, blank=True, null=True)
    data_source_db = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'np_assay'


class GenericDrugData(models.Model):
    serial_number = models.TextField(blank=True, null=True, verbose_name='序号')
    generic_name = models.TextField(blank=True, null=True, verbose_name='药品通用名称')  #
    english_name_or_trade = models.TextField(blank=True, null=True, verbose_name='英文名称/商品名')  #
    specifications = models.TextField(blank=True, null=True, verbose_name='规格')  #
    dosage_form = models.TextField(blank=True, null=True, verbose_name='剂型')  #
    holder = models.TextField(blank=True, null=True, verbose_name='持证商')  #
    remarks1 = models.TextField(blank=True, null=True, verbose_name='备注1')
    remarks2 = models.TextField(blank=True, null=True, verbose_name='备注2')
    information_sources = models.TextField(blank=True, null=True, verbose_name='信息来源')  #

    class Meta:
        db_table = 'genericDrugData'


class InactiveIngredientSearch(models.Model):
    inactive_ingredient = models.TextField(blank=True, null=True)
    route = models.TextField(blank=True, null=True)
    dosage_form = models.TextField(blank=True, null=True)
    cas_number = models.TextField(blank=True, null=True)
    UNII = models.TextField(blank=True, null=True)
    maximum_potency_per_unit_dose = models.TextField(blank=True, null=True)
    record_updated = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'Inactive Ingredient Search for Approved Drug Product_all'


class FDAdrug(models.Model):
    trade_name = models.TextField(blank=True, null=True, verbose_name='商品名')
    application_number = models.TextField(blank=True, null=True, verbose_name='申请号')
    product_id = models.TextField(blank=True, null=True, verbose_name='产品号')
    application_type = models.TextField(blank=True, null=True, verbose_name='申请类型')
    active_ingredient = models.TextField(blank=True, null=True, verbose_name='活性成分')
    dosage_form_or_route_of_administration = models.TextField(blank=True, null=True, verbose_name='剂型/给药途径')
    specification_or_dosage = models.TextField(blank=True, null=True, verbose_name='规格/剂量')
    RLD = models.TextField(blank=True, null=True)
    RS = models.TextField(blank=True, null=True)
    application_No_original_or_tentative_approval_date = models.TextField(blank=True, null=True,
                                                                          verbose_name='申请号原始批准/暂定批准日期')
    product_number_approval_date = models.TextField(blank=True, null=True, verbose_name='产品号批准日期')
    applicant = models.TextField(blank=True, null=True, verbose_name='申请人')
    market_state = models.TextField(blank=True, null=True, verbose_name='市场状态')

    class Meta:
        db_table = 'USA_FDA_drug_db'


class FDAdrugOrangeBook(models.Model):
    trade_name = models.TextField(blank=True, null=True, verbose_name='商品名')
    application_number = models.TextField(blank=True, null=True, verbose_name='申请号')
    product_id = models.TextField(blank=True, null=True, verbose_name='产品号')
    application_type = models.TextField(blank=True, null=True, verbose_name='申请类型')
    active_ingredient = models.TextField(blank=True, null=True, verbose_name='活性成分')
    dosage_form_or_route_of_administration = models.TextField(blank=True, null=True, verbose_name='剂型/给药途径')
    specification_or_dosage = models.TextField(blank=True, null=True, verbose_name='规格/剂量')
    reference_drug_or_not = models.TextField(blank=True, null=True, verbose_name='是否参比药物')
    bioequivalence_reference_standard_or_not = models.TextField(blank=True, null=True, verbose_name='是否生物等效参考标准')
    treatment_equivalent_code = models.TextField(blank=True, null=True, verbose_name='治疗等效代码')
    product_batch_date = models.TextField(blank=True, null=True, verbose_name='产品批次日期')
    applicant = models.TextField(blank=True, null=True, verbose_name='申请人')
    market_state = models.TextField(blank=True, null=True, verbose_name='市场状态')

    class Meta:
        db_table = 'USA_FDA_drug_orange_book_db'


class ClinicalDataBig(models.Model):
    url = models.TextField(blank=True, null=True)
    other_study_id_numbers = models.TextField(blank=True, null=True)
    trial_id = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    sponsor = models.TextField(blank=True, null=True)
    agency_class = models.TextField(blank=True, null=True)
    information_provider = models.TextField(blank=True, null=True)
    brief_summary = models.TextField(blank=True, null=True)
    detailed_description = models.TextField(blank=True, null=True)
    recruitment_status = models.TextField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    study_type = models.TextField(blank=True, null=True)
    intervention_model = models.TextField(blank=True, null=True)
    study_design_primary_purpose = models.TextField(blank=True, null=True)
    study_design_masking = models.TextField(blank=True, null=True)
    target_disease = models.TextField(blank=True, null=True)
    intervention_type = models.TextField(blank=True, null=True)
    interventions = models.TextField(blank=True, null=True)
    criteria = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    minimum_age = models.TextField(blank=True, null=True)
    maximum_age = models.TextField(blank=True, null=True)
    healthy_volunteers = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    measure_outcome = models.TextField(blank=True, null=True)
    study_design = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'clinical_data_big'


class FDAPatent(models.Model):
    patent_number = models.TextField(blank=True, null=True)
    patent_link = models.TextField(blank=True, null=True)
    patent_expiration_date = models.TextField(blank=True, null=True)
    application_number = models.TextField(blank=True, null=True)
    product_id = models.TextField(blank=True, null=True)
    trade_name = models.TextField(blank=True, null=True)
    active_ingredient = models.TextField(blank=True, null=True)
    dosage_form = models.TextField(blank=True, null=True)
    material_patent = models.TextField(blank=True, null=True)
    product_patent = models.TextField(blank=True, null=True)
    use_patent = models.TextField(blank=True, null=True)
    detail_link = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'FDAPatent'


class ChemicalIndex(models.Model):
    title = models.TextField(blank=True, null=True)
    CAS_registry_number = models.TextField(blank=True, null=True)
    CAS_name = models.TextField(blank=True, null=True)
    additional_names = models.TextField(blank=True, null=True)
    manufacturers_codes = models.TextField(blank=True, null=True)
    molecular_formula = models.TextField(blank=True, null=True)
    molecular_weight = models.TextField(blank=True, null=True)
    percent_composition = models.TextField(blank=True, null=True)
    literature_references = models.TextField(blank=True, null=True)
    properties = models.TextField(blank=True, null=True)
    melting_point = models.TextField(blank=True, null=True)
    pKa = models.TextField(blank=True, null=True)
    optical_rotation = models.TextField(blank=True, null=True)
    logP = models.TextField(blank=True, null=True)
    absorption_maximum = models.TextField(blank=True, null=True)
    therap_cat = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    toxicity_data = models.TextField(blank=True, null=True)
    derivative_type = models.TextField(blank=True, null=True)
    derivativeCASRegistryNumber = models.TextField(blank=True, null=True)
    derivativeTrademarks = models.TextField(blank=True, null=True)
    derivativeMolecularFormula = models.TextField(blank=True, null=True)
    derivativeMolecularWeight = models.TextField(blank=True, null=True)
    derivativePercentComposition = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'ChemicalIndex'

# class YearEndData(models.Model):
#     drug_name = models.TextField(db_column='Drug_Name', blank=True, null=True)  # Field name made lowercase.
#     other_drug_names = models.TextField(db_column='Other_Drug_Names', blank=True,
#                                         null=True)  # Field name made lowercase.
#     originator_company = models.TextField(db_column='Originator_Company', blank=True,
#                                           null=True)  # Field name made lowercase.
#     active_companies = models.TextField(db_column='Active_Companies', blank=True,
#                                         null=True)  # Field name made lowercase.
#     active_indications = models.TextField(db_column='Active_Indications', blank=True,
#                                           null=True)  # Field name made lowercase.
#     target_based_actions = models.TextField(db_column='Target_based_Actions', blank=True,
#                                             null=True)  # Field name made lowercase.
#     highest_status = models.TextField(db_column='Highest_Status', blank=True, null=True)  # Field name made lowercase.
#     technologies = models.TextField(db_column='Technologies', blank=True, null=True)  # Field name made lowercase.
#     total_reported_sales_2014_usd_m = models.TextField(db_column='Total_Reported_Sales_2014_USD_M', blank=True,
#                                                        null=True)  # Field name made lowercase.
#     total_forecast_sales_2020_usd_m = models.TextField(db_column='Total_Forecast_Sales_2020_USD_M', blank=True,
#                                                        null=True)  # Field name made lowercase.
#     inactive_companies = models.TextField(db_column='Inactive_Companies', blank=True,
#                                           null=True)  # Field name made lowercase.
#     inactive_indications = models.TextField(db_column='Inactive_Indications', blank=True,
#                                             null=True)  # Field name made lowercase.
#     other_actions = models.TextField(db_column='Other_Actions', blank=True, null=True)  # Field name made lowercase.
#     last_change_date = models.TextField(db_column='Last_Change_Date', blank=True,
#                                         null=True)  # Field name made lowercase.
#
#     class Meta:
#         db_table = 'my_search_yearenddata'
# class ClinicalData(models.Model):
#     title = models.TextField(blank=True, null=True)
#     summary = models.TextField(blank=True, null=True)
#     status = models.TextField(blank=True, null=True)
#     phase = models.TextField(blank=True, null=True)
#     condation = models.TextField(blank=True, null=True)
#     intervention = models.TextField(blank=True, null=True)
#     location = models.TextField(blank=True, null=True)
#
#     class Meta:
#         db_table = 'clinical_data'
