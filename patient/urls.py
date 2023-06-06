from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('patient_registration/', views.PatientRegistrationList.as_view()),
    path('patient_registration/<int:pk>/', views.PatientRegistrationDetail.as_view()),
    path('appointment_receptionist/', views.AppointmentReceptionistList.as_view()),
    path('appointment_receptionist/<int:pk>/', views.AppointmentReceptionistDetail.as_view()),
    path('prescription_therapist/', views.PrescriptionTherapistList.as_view()),
    path('prescription_therapist/<int:pk>/', views.PrescriptionTherapistDetail.as_view()),
    path('patient_bill/', views.PatientBillList.as_view()),
    path('patient_bill/<int:pk>/', views.PatientBillDetail.as_view()),
    path('prescription_physiotherapy_assistant/', views.PrescriptionPhysioTherapyAssistantList.as_view()),
    path('prescription_physiotherapy_assistant/<int:pk>/', views.PrescriptionPhysioTherapyAssistantDetail.as_view()),

    path('National_ID_Typedata/', views.National_ID_Typedata, name='National_ID_Typedata'),
    path('Patient_Genderdata/', views.Patient_Genderdata, name='Patient_Genderdata'),
    path('Marital_Statusdata/', views.Marital_Statusdata, name='Marital_Statusdata'),

    path('National_ID_Typedata/', views.National_ID_Typedata, name='National_ID_Typedata'),
    path('Educationdata/', views.Educationdata, name='Educationdata'),
    path('Economic_Sub_Sector_Code_ISICdaat/', views.Economic_Sub_Sector_Code_ISICdaat, name='Economic_Sub_Sector_Code_ISICdaat'),
     path('Legal_Statusdata/', views.Legal_Statusdata, name='Legal_Statusdata'),
    path('Patient_Statusdata/', views.Patient_Statusdata, name='Patient_Statusdata'),
    path('Countrydata/', views.Countrydata, name='Countrydata'),
    path('Provincedata/', views.Provincedata, name='Provincedata'),
    path('Districtdata/', views.Districtdata, name='Districtdata'),
    path('Sectordata/', views.Sectordata, name='Sectordata'),
    path('Celldata/', views.Celldata, name='Celldata'),
    path('Villagedata/', views.Villagedata, name='Villagedata'),
    path('dashbord/', views.DashboardView.as_view()),

    path('home', views.home, name='home'),
    path('', views.login, name='login'),
    path('calendar', views.calendar, name='calendar'),
    path('contact', views.contact, name='contact'),
    path('form_advanced', views.form_advanced, name='form_advanced'),
    path('form_wizards', views.form_wizards, name='form_wizards'),
    path('invoice', views.invoice, name='invoice'),
    path('profile', views.profile, name='profile'),
    path('tables_dynamic', views.tables_dynamic, name='tables_dynamic'),
    path('tables', views.tables, name='tables'),

    # AdminDashbord for THERAPIST
    path('TherapistHome', views.TherapistHome, name='TherapistHome'),
    path('TherapistCalendar', views.TherapistCalendar, name='TherapistCalendar'),
    path('TherapistContact', views.TherapistContact, name='TherapistContact'),
    path('TherapistForm_wizards', views.TherapistForm_wizards, name='TherapistForm_wizards'),
    path('TherapistInvoice', views.TherapistInvoice, name='TherapistInvoice'),
    path('TherapistProfile', views.TherapistProfile, name='TherapistProfile'),
    path('TherapistTables_dynamic', views.TherapistTables_dynamic, name='TherapistTables_dynamic'),
    path('TherapistTables', views.TherapistTables, name='TherapistTables'),
    path('TherapistForm_advanced', views.TherapistForm_advanced, name='TherapistForm_advanced'),

    # AdminDashbord for Assistance
    path('AssistanceHome', views.AssistanceHome, name='AssistanceHome'),
    path('AssistanceCalendar', views.AssistanceCalendar, name='AssistanceCalendar'),
    path('AssistanceContact', views.AssistanceContact, name='AssistanceContact'),
    path('AssistanceForm_advanced', views.AssistanceForm_advanced, name='AssistanceForm_advanced'),
    path('AssistanceForm_wizards', views.AssistanceForm_wizards, name='AssistanceForm_wizards'),
    path('AssistanceInvoice', views.AssistanceInvoice, name='AssistanceInvoice'),
    path('AssistanceProfile', views.AssistanceProfile, name='AssistanceProfile'),
    path('TherapistTables_dynamic', views.TherapistTables_dynamic, name='TherapistTables_dynamic'),
    path('AssistanceTables', views.AssistanceTables, name='AssistanceTables'),
    




  
   
   
]
