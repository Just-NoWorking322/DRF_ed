# from django.views.generic import CreateView
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView, UpdateAPIView
from apps.main.models import Settings, Main, About, Contact, Form, ProductImage, Products
from apps.main.serializer import SettingsSerializer, MainSerializer, AboutSerializer, ContactSerializer, FormSerializer, ProductSerializer, ProductImageSerializer

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

class ProductCreateView(CreateAPIView):
    queryset = Products
    serializer_class = ProductSerializer

class ProductListView(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductDeleteView(DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer