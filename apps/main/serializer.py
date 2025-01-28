from rest_framework import serializers
from apps.main.models import Settings, Main, About, Contact, Form

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = "__all__"

class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = "__all__"

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = "__all__"

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = "__all__"