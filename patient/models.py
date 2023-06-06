import random

from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils import timezone

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_CHOICES = [
        ('Terapist', 'Terapist'),
        ('Assistence', 'Assistence'),
        ('Receptionist', 'Receptionist'),
        ('Admin', 'Admin')
    ]
    user_type = models.CharField(choices=USER_CHOICES, max_length=40, blank=True,null=True)
    # image = models.ImageField(upload_to='MEDIA',blank=True,null=True)

    def is_terapist(self):
        return self.user_type == 'Terapist'
    
    def is_assistence(self):
        return self.user_type == 'Assistence'

    def is_receptionist(self):
        return self.user_type == 'Receptionist'

    def is_admin(self):
        return self.user_type == 'Admin'

    class Meta:
        ordering = ('id',)
    
    # add related_name to avoid reverse accessor clash with patient.User.groups
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='auth_users',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
    )

    # add related_name to avoid reverse accessor clash with patient.User.user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='auth_users',
        blank=True,
        help_text='Specific permissions for this user.'
    )




class National_ID_Type(models.Model):
   ID_Type =models.CharField(primary_key=True,max_length=80, blank=True, null=False)
   interface = models.CharField(max_length=25, blank=True, null=False)


   def __str__(self):
       return self.ID_Type
   class Meta:
       db_table = 'National_ID_Type'




class Patient_Gender(models.Model):
   Gender= models.CharField(primary_key=True,max_length=15, blank=True, null=False)
   GenderDescription= models.CharField(max_length=15, blank=True, null=False)
   interface= models.CharField(max_length=15, blank=True, null=False)


   def __str__(self):
       return self.Gender
   class Meta:
       db_table = 'Customer_Gender'


class Marital_Status(models.Model):
   Marital_Status=  models.CharField(primary_key=True,max_length=5, blank=True, null=False)
   Marital_Status_Description =  models.CharField(max_length=20, blank=True, null=False)
   interface= models.CharField(max_length=15, blank=True, null=False)


   def __str__(self):
       return self.Marital_Status_Description
   class Meta:
       db_table = 'Marital_Status'


class Education(models.Model):
   Education_Description= models.CharField(primary_key=True, max_length=255, blank=True, null=False)
   interface= models.CharField(max_length=15, blank=True, null=False)


   def __str__(self):
       return self.Education_Description
   class Meta:
       db_table = 'Education'


class Economic_Sub_Sector_Code_ISIC(models.Model):
   ECONOMIC_SUB_SECTOR_CODE_ISIC = models.CharField(primary_key=True,max_length=5, blank=True, null=False)
   ECONOMIC_SUB_SECTOR_CODE_ISIC_DESC= models.CharField(max_length=255, blank=True, null=False)


   def __str__(self):
       return self.ECONOMIC_SUB_SECTOR_CODE_ISIC_DESC
   class Meta:
       db_table = 'Economic_Sub_Sector_Code_ISIC'


class Legal_Status(models.Model):
   Legal_Status= models.CharField(primary_key=True, max_length=1, blank=True, null=False)
   Legal_Status_Description= models.CharField(max_length=80, blank=True, null=False)


   def __str__(self):
       return self.Legal_Status_Description
   class Meta:
       db_table = 'Legal_Status'


class Patient_Status(models.Model):
   General_Status= models.CharField(primary_key=True,max_length=1, blank=True, null=False)
   General_Status_Description= models.CharField(max_length=10, blank=True, null=False)


   def __str__(self):
       return self.General_Status_Description
   class Meta:
       db_table = 'Customer_Status'


class Country(models.Model):
   country = models.CharField(max_length=2, blank=False,null=False)
   Country_Description = models.CharField(max_length=80, blank=False,null=False)




   def __str__(self) -> str:
       return self.Country_Description
   class Meta:
       db_table = 'Country'


class Province(models.Model):
   Province_List =  models.CharField(primary_key=True,unique=True, max_length=10, blank=False,null=False)
   Province_List_Description = models.CharField(max_length=80,blank=False,null=True)
   def __str__(self) -> str:
       return self.Province_List_Description
   class Meta:
       db_table = 'Province'

    
class District(models.Model):
   District_List = models.CharField(primary_key=True,unique=True, max_length=10, blank=False,null=False) 
   District_List_Description =  models.CharField(max_length=80, blank=False,null=False)
   Province_List = models.ForeignKey(Province, on_delete=models.PROTECT,max_length=10, blank=False,null=False)
   Province_List_Description = models.CharField(max_length=80, blank=False,null=False)
  
   def __str__(self) -> str:
       return self.District_List_Description

   class Meta:
       db_table = 'District'

class Sector(models.Model):
   Sector_List = models.CharField(primary_key=True,unique=True, max_length=10, blank=False,null=False)
   Sector_List_Description = models.CharField(max_length=80, blank=False, null=False)
   District_List = models.ForeignKey(District,max_length=10, on_delete=models.PROTECT, blank=False,null=False)
   District_List_Description = models.CharField(max_length=80, blank=False,null=False)


   def __str__(self) -> str:
       return self.Sector_List_Description
  
   class Meta:
       db_table = 'Sector'
 
class Cell(models.Model):
   Cell_List = models.CharField(primary_key=True,unique=True, max_length=10, blank=False, null=False)
   Cell_List_Description = models.CharField(max_length=80, blank=False, null=False)
   Sector_List = models.ForeignKey(Sector, on_delete=models.PROTECT, blank=False, null=False)
   Sector_List_Description = models.CharField(max_length=80, blank=False, null=False)
  
   def __str__(self) -> str:
       return self.Cell_List_Description


   class Meta:
       db_table = 'Cell'


class Village(models.Model):
   Village_List = models.CharField(primary_key=True,unique=True, max_length=20, blank=False, null=False)
   Vilage_List_Description = models.CharField(max_length=80, blank=False, null=False)
   Cell_List = models.ForeignKey(Cell, on_delete=models.PROTECT, blank=False,null=False)
   Cell_List_Description =  models.CharField(max_length=40, blank=False, null=False)


   def __str__(self) -> str:
       return self.Vilage_List_Description


   class Meta:
       db_table = 'Village'


class PatientRegistration(models.Model):

   patient_ID = models.CharField(primary_key=True, max_length=70, null=False,blank=True)
   National_ID_Typ = models.ForeignKey(National_ID_Type,related_name='National_ID_Typ', on_delete=models.PROTECT, max_length=4,blank=True,null=True)
   National_ID_Number = models.CharField(max_length=16, blank=True,null=True, unique=True)
   patient_Name = models.CharField(max_length=80, blank=True, null=True)
   FirstName = models.CharField(max_length=80, blank=True, null=True)
   LastName = models.CharField(max_length=80,blank=True, null=True)
   patient_registed_Date = models.DateTimeField(default = timezone.now)
   patient_Gender = models.ForeignKey(Patient_Gender,on_delete=models.PROTECT, max_length=10,blank=True, null=True)
   Date_of_Birth = models.DateField(default = timezone.now)
   Place_of_Birth = models.ForeignKey(Country,related_name='Place_of_Birth', on_delete=models.PROTECT, max_length=80, blank=True, null=True)
   Marital_Status = models.ForeignKey(Marital_Status,on_delete=models.PROTECT,max_length=10,blank=True, null=True)
   Nationality = models.ForeignKey(Country,related_name='nationality', on_delete=models.PROTECT, blank=True,null=True)
   Residence = models.ForeignKey(Country, on_delete=models.PROTECT, blank=True,null=True) 
   province = models.ForeignKey(Province,related_name='province', on_delete=models.PROTECT, max_length=10,blank=True, null=True) 
   district = models.ForeignKey(District,related_name='district', on_delete=models.PROTECT, max_length=10,blank=True, null=True)
   sector = models.ForeignKey(Sector,related_name='sector', on_delete=models.PROTECT, max_length=10,blank=True, null=True)
   cell = models.ForeignKey(Cell,related_name='cell', on_delete=models.PROTECT, max_length=10,blank=True, null=True)
   village = models.ForeignKey(Village,related_name='Comm_Village', on_delete=models.PROTECT, max_length=10,blank=True, null=True)
   Email_ID = models.EmailField(max_length=100, blank=True, null=True)
   Telephone = models.CharField(max_length=20, blank=True, null=True)
   Education = models.ForeignKey(Education, on_delete=models.CASCADE, max_length=4,blank=True,null=True)
   Economic_Sub_Sector = models.ForeignKey(Economic_Sub_Sector_Code_ISIC, on_delete=models.CASCADE, max_length=10,blank=True,null=True)
   Legal_Status = models.ForeignKey(Legal_Status,on_delete=models.CASCADE, max_length=4,blank=True, null=True)
   patient_Status = models.ForeignKey(Patient_Status,on_delete=models.CASCADE, max_length=4,blank=True, null=True)

   def __str__(self) -> str:
       return f'{self.patient_Name}, WITH THIS ID: {self.patient_ID}'
  
   class Meta:
       db_table = 'PatientRegistration'


class Appointment_Receptionist(models.Model):
   patient = models.ForeignKey(PatientRegistration, on_delete=models.CASCADE, related_name='patient',blank=True, null=True)
   patient_id_number = models.CharField(max_length=200,blank=True, null=True)
   date = models.DateField(blank=True, null=True)
   time = models.DateTimeField(default=timezone.now,blank=True, null=True)
   status = models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=10,blank=True, null=True)
   therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='therapist',blank=True, null=True)
  

   def __str__(self):
       return "Patient - {} Ther- {} At {} {}".format(self.patient, self.therapist, self.date, self.time)


class Prescription_Therapist(models.Model):
   therapist = models.ForeignKey(User, on_delete=models.CASCADE, related_name='therapist_prescription',blank=True, null=True)
   patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='patient_prescription',blank=True, null=True)
   date = models.DateField(auto_now_add=True,blank=True, null=True)
   symptoms = models.CharField(max_length=200,blank=True, null=True)
   prescription = models.TextField(blank=True, null=True)

   class Meta:
       ordering = ('-id',)


   def __str__(self):
       return "Presciption Ther-{} Patient-{}".format(self.therapist, self.patient)


class PatientBill(models.Model):
   patient = models.ForeignKey(PatientRegistration, related_name='patientbillbycustomer', on_delete=models.CASCADE,blank=True, null=True)
   treatment_date = models.DateTimeField(default=timezone.now)
   amount = models.FloatField(blank=True, null=True)
   payment_date = models.DateTimeField(default=timezone.now,blank=True, null=True)
  
   def __str__(self):
       return self.patient


class Prescription_PhysioTherapy_ASSISTANT(models.Model):
   assistant = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assistance_prescription',blank=True, null=True)
   patient = models.ForeignKey(PatientRegistration, on_delete=models.CASCADE, related_name='patient_prescription',blank=True, null=True)
   date = models.DateField(auto_now_add=True)
   symptoms = models.CharField(max_length=200,blank=True, null=True)
   prescription = models.TextField(blank=True, null=True)


   class Meta:
       ordering = ('-id',)


   def __str__(self):
       return "Presciption Ther-{} Patient-{}".format(self.assistant, self.patient)
