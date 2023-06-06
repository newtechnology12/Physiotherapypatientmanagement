from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

admin.site.register(PatientRegistration)
@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ('country','Country_Description')


class ProvinceResources(resources.ModelResource):
    class Meta:
        model = Province
        import_id_fields = ('Province_List',)
        fields =('Province_List','Province_List_Description',)

@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin):
    resource_class = ProvinceResources
    list_display = ('Province_List','Province_List_Description')

class DistrictAdmin(resources.ModelResource):
    class Meta:
        model = District
        import_id_fields = ('District_List',)
        fields = ('District_List','District_List_Description','Province_List','Province_List_Description',)

@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin):
    resource_class = DistrictAdmin
    list_display = ('District_List','District_List_Description','Province_List','Province_List_Description')

class Sectorresources(resources.ModelResource):
    class Meta:
        model = Sector
        import_id_fields = ('Sector_List',)
        fields = ('Sector_List','Sector_List_Description','District_List','District_List_Description',)
@admin.register(Sector)
class SectorAdmin(ImportExportModelAdmin):
    resource_class = Sectorresources
    list_display = ('Sector_List','Sector_List_Description','District_List','District_List_Description')


class CellResources(resources.ModelResource):
    class Meta:
        model = Cell
        import_id_fields = ('Cell_List',)
        fields = ('Cell_List','Cell_List_Description','Sector_List','Sector_List_Description',)
        
@admin.register(Cell)
class CellAdmin(ImportExportModelAdmin):
    resource_class = CellResources
    list_display = ('Cell_List','Cell_List_Description','Sector_List','Sector_List_Description')
class VillageResources(resources.ModelResource):
    class Meta:
        model = Village
        import_id_fields = ('Village_List',)
        fields = ('Village_List','Vilage_List_Description','Cell_List','Cell_List_Description',)

@admin.register(Village)
class VillageAdmin(ImportExportModelAdmin):
    resource_class = VillageResources
    list_display = ('Village_List','Vilage_List_Description','Cell_List','Cell_List_Description')

class EducationResource(resources.ModelResource):
    class Meta:
        model = Education
        import_id_fields = ('Education_Description',)
        fields = ('Education_Description','interface',) 

@admin.register(Education)
class EducationAdmin(ImportExportModelAdmin):
    resource_class = EducationResource
    list_display = ('Education_Description','interface')

class CustomerResources(resources.ModelResource):
    class Meta:
        model =Patient_Status
        import_id_fields = ('General_Status',)
        fields = ('General_Status','General_Status_Description',)
@admin.register(Patient_Status)
class CustomerAdmin(ImportExportModelAdmin):
    resource_class = CustomerResources
    list_display = ('General_Status','General_Status_Description')

class Legal_StatusResources(resources.ModelResource):
    class Meta:
        model = Legal_Status
        import_id_fields = ('Legal_Status',)
        fields = ('Legal_Status','Legal_Status_Description',)

@admin.register(Legal_Status)
class Legal_StatusAdmin(ImportExportModelAdmin):
    resource_class = Legal_StatusResources
    list_display = ('Legal_Status','Legal_Status_Description')


class Economic_Sub_Sector_Code_ISICResources(resources.ModelResource):
    class Meta:
        model = Economic_Sub_Sector_Code_ISIC
        import_id_fields = ('ECONOMIC_SUB_SECTOR_CODE_ISIC',)
        fields = ('ECONOMIC_SUB_SECTOR_CODE_ISIC','ECONOMIC_SUB_SECTOR_CODE_ISIC_DESC',)

@admin.register(Economic_Sub_Sector_Code_ISIC)
class Economic_Sub_Sector_Code_ISICAdmin(ImportExportModelAdmin):
    resource_class = Economic_Sub_Sector_Code_ISICResources
    list_display = ('ECONOMIC_SUB_SECTOR_CODE_ISIC','ECONOMIC_SUB_SECTOR_CODE_ISIC_DESC')


class Marital_StatusResources(resources.ModelResource):
    class Meta:
        model = Marital_Status
        import_id_fields = ('Marital_Status',)
        fields = ('Marital_Status','Marital_Status_Description','interface',)
@admin.register(Marital_Status)
class Marital_StatusAdmin(ImportExportModelAdmin):
    resource_class = Marital_StatusResources
    list_display = ('Marital_Status','Marital_Status_Description','interface')


class Customer_GenderResource(resources.ModelResource):

    class Meta:
        model = Patient_Gender
        import_id_fields = ('Gender',)
        fields = ('Gender','GenderDescription','interface',) 

@admin.register(Patient_Gender)
class Customer_GenderAdmin(ImportExportModelAdmin):
    resource_class = Customer_GenderResource
    list_display = ('Gender','GenderDescription','interface')


class National_ID_TypeResources(resources.ModelResource):
    class Meta:
        model = National_ID_Type
        import_id_fields = ('ID_Type',)
        fields = ('ID_Type','interface',)

@admin.register(National_ID_Type)
class National_ID_TypeAdmin(ImportExportModelAdmin):
    resource_class = National_ID_TypeResources
    list_display = ('ID_Type','interface')


admin.site.register(Appointment_Receptionist)
admin.site.register(Prescription_Therapist)
admin.site.register(PatientBill)
admin.site.register(User)
admin.site.register(Prescription_PhysioTherapy_ASSISTANT)
# admin.site.register(PatientRegistration)
