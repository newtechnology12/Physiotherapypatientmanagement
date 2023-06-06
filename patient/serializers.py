from rest_framework import serializers
from .models import User, PatientRegistration, Appointment_Receptionist, Prescription_Therapist, PatientBill, Prescription_PhysioTherapy_ASSISTANT

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission

User = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    user_permissions = PermissionSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'groups', 'user_permissions', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            # image = validated_data['image'],
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            user_type=validated_data['user_type'],
            password=validated_data['password']
        )

        groups = validated_data.get('groups')
        if groups:
            for group in groups:
                group_obj = Group.objects.get(id=group['id'])
                user.groups.add(group_obj)

        user_permissions = validated_data.get('user_permissions')
        if user_permissions:
            for permission in user_permissions:
                permission_obj = Permission.objects.get(id=permission['id'])
                user.user_permissions.add(permission_obj)

        return user


class PatientRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientRegistration
        fields = '__all__'


class AppointmentReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment_Receptionist
        fields = '__all__'


class PrescriptionTherapistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription_Therapist
        fields = '__all__'


class PatientBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientBill
        fields = '__all__'


class PrescriptionPhysioTherapyAssistantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription_PhysioTherapy_ASSISTANT
        fields = '__all__'
