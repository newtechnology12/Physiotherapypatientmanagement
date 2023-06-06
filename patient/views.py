from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
from rest_framework import generics,status
from .models import *
from .serializers import UserSerializer, PatientRegistrationSerializer, AppointmentReceptionistSerializer, PrescriptionTherapistSerializer, PatientBillSerializer, PrescriptionPhysioTherapyAssistantSerializer
from rest_framework.response import Response
from django.db.models import Count



class DashboardView(generics.ListAPIView):
    serializer_class = None  # We don't need a serializer, so set to None

    def list(self, request, *args, **kwargs):
        patient_count = PatientRegistration.objects.count()
        appointment_count = Appointment_Receptionist.objects.count()
        prescription_count = Prescription_Therapist.objects.count()
        bill_count = PatientBill.objects.count()

        patient_by_gender = PatientRegistration.objects.values('patient_Gender').annotate(count=Count('patient_Gender'))
        appointment_by_day = Appointment_Receptionist.objects.values('date').annotate(count=Count('date'))
        prescription_by_type = Prescription_Therapist.objects.values('symptoms').annotate(count=Count('symptoms'))

        context = {
            'patient_count': patient_count,
            'appointment_count': appointment_count,
            'prescription_count': prescription_count,
            'bill_count': bill_count,
            'patient_by_gender': patient_by_gender,
            'appointment_by_day': appointment_by_day,
            'prescription_by_type': prescription_by_type,
        }

        return Response(context, status=status.HTTP_200_OK)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PatientRegistrationList(generics.ListCreateAPIView):
    queryset = PatientRegistration.objects.all()
    serializer_class = PatientRegistrationSerializer


class PatientRegistrationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientRegistration.objects.all()
    serializer_class = PatientRegistrationSerializer


class AppointmentReceptionistList(generics.ListCreateAPIView):
    queryset = Appointment_Receptionist.objects.all()
    serializer_class = AppointmentReceptionistSerializer


class AppointmentReceptionistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Appointment_Receptionist.objects.all()
    serializer_class = AppointmentReceptionistSerializer


class PrescriptionTherapistList(generics.ListCreateAPIView):
    queryset = Prescription_Therapist.objects.all()
    serializer_class = PrescriptionTherapistSerializer


class PrescriptionTherapistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription_Therapist.objects.all()
    serializer_class = PrescriptionTherapistSerializer


class PatientBillList(generics.ListCreateAPIView):
    queryset = PatientBill.objects.all()
    serializer_class = PatientBillSerializer


class PatientBillDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientBill.objects.all()
    serializer_class = PatientBillSerializer


class PrescriptionPhysioTherapyAssistantList(generics.ListCreateAPIView):
    queryset = Prescription_PhysioTherapy_ASSISTANT.objects.all()
    serializer_class = PrescriptionPhysioTherapyAssistantSerializer


class PrescriptionPhysioTherapyAssistantDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Prescription_PhysioTherapy_ASSISTANT.objects.all()
    serializer_class = PrescriptionPhysioTherapyAssistantSerializer


# filter thirdpary based on vehicle type
def National_ID_Typedata(request):
    thirdparty = list(National_ID_Type.objects.values()) # fetch data from MyModel and convert to list
    return JsonResponse(thirdparty, safe=False) # return JSON response


def Patient_Genderdata(request):
    duration = list(Patient_Gender.objects.values()) # fetch data from MyModel and convert to list
    return JsonResponse(duration, safe=False) # return JSON response


def Marital_Statusdata (request):
    owndamage  = list(Marital_Status.objects.values())
    return JsonResponse(owndamage, safe=False)

def Educationdata (request):
    theft =  list(Education.objects.values())
    return JsonResponse(theft, safe=False)


def Economic_Sub_Sector_Code_ISICdaat(request):
    fire = list(Economic_Sub_Sector_Code_ISIC.objects.values())
    return JsonResponse(fire, safe=False)


def Legal_Statusdata(request):
    excess = list(Legal_Status.objects.values())
    return JsonResponse(excess, safe=False)

def Patient_Statusdata(request):
    occupant = list(Patient_Status.objects.values())
    return JsonResponse(occupant, safe=False)

def Countrydata(request):
    fees = list(Country.objects.values())
    return JsonResponse(fees, safe=False)


def Marital_Statusdata (request):
    owndamage  = list(Marital_Status.objects.values())
    return JsonResponse(owndamage, safe=False)

def Provincedata (request):
    theft =  list(Province.objects.values())
    return JsonResponse(theft, safe=False)


def Districtdata(request):
    fire = list(District.objects.values())
    return JsonResponse(fire, safe=False)


def Sectordata(request):
    excess = list(Sector.objects.values())
    return JsonResponse(excess, safe=False)

def Celldata(request):
    occupant = list(Cell.objects.values())
    return JsonResponse(occupant, safe=False)

def Villagedata(request):
    fees = list(Village.objects.values())
    return JsonResponse(fees, safe=False)

def home(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/index3.html')

def login(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/login.html')

def calendar(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/calendar.html')

def contact(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/contacts.html')

def form_advanced(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/form_advanced.html')

def form_wizards(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/form_wizards.html')

def invoice(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/invoice.html')

def profile(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/profile.html')
def tables_dynamic(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/tables_dynamic.html')

def tables(request):
    return render(request, 'AdminDashbordRECEPTIONIST/production/tables.html')

# AdminDashbord for THERAPIST

def TherapistHome(request):
    return render(request, 'AdminDashbordTHERAPIST/production/index3.html')

def TherapistLogin(request):
    return render(request, 'AdminDashbordTHERAPIST/production/login.html')

def TherapistCalendar(request):
    return render(request, 'AdminDashbordTHERAPIST/production/calendar.html')

def TherapistContact(request):
    return render(request, 'AdminDashbordTHERAPIST/production/contacts.html')

def TherapistForm_advanced(request):
    return render(request, 'AdminDashbordTHERAPIST/production/form_advanced.html')

def TherapistForm_wizards(request):
    return render(request, 'AdminDashbordTHERAPIST/production/form_wizards.html')

def TherapistInvoice(request):
    return render(request, 'AdminDashbordTHERAPIST/production/invoice.html')

def TherapistProfile(request):
    return render(request, 'AdminDashbordTHERAPIST/production/profile.html')

def TherapistTables_dynamic(request):
    return render(request, 'AdminDashbordTHERAPIST/production/tables_dynamic.html')

def TherapistTables(request):
    return render(request, 'AdminDashbordTHERAPIST/production/tables.html')


# AdminDashbord for Assistance

def AssistanceHome(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/index3.html')

def AssistanceLogin(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/login.html')

def AssistanceCalendar(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/calendar.html')

def AssistanceContact(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/contacts.html')

def AssistanceForm_advanced(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/form_advanced.html')

def AssistanceForm_wizards(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/form_wizards.html')

def AssistanceInvoice(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/invoice.html')

def AssistanceProfile(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/profile.html')

def TherapistTables_dynamic(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/tables_dynamic.html')

def AssistanceTables(request):
    return render(request, 'AdminDashbordPHYSIOTHERAPY_ASSISTANT/production/tables.html')