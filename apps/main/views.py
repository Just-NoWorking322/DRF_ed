# from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView # type: ignore
from apps.main.models import Settings, Main, About, Contact, Form
from apps.main.serializer import SettingsSerializer, MainSerializer, AboutSerializer, ContactSerializer, FormSerializer

class CreateSettingsView(CreateAPIView):
    queryset = Settings.objects.all()
    main = Main.objects.all()
    serializer_class = SettingsSerializer

class CreateMainView(CreateAPIView):
    queryset = Main.objects.all()
    main = Main.objects.all()
    serializer_class = MainSerializer

class CreateAboutView(CreateAPIView):
    queryset = About.objects.all()
    main = Main.objects.all()
    serializer_class = AboutSerializer

class CreateContactView(CreateAPIView):
    queryset = Contact.objects.all()
    main = Main.objects.all()
    serializer_class = ContactSerializer

class CreateFormView(CreateAPIView):
    queryset = Form.objects.all()
    main = Main.objects.all()
    serializer_class = FormSerializer 
    