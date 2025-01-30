from rest_framework import serializers
from apps.main.models import Settings, Main, About, Contact, Form, ProductImage, Products

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

class ProductImageSerializer(serializers.ModelSerializer):
    image =serializers.ImageField()
    
    class Meta:
        model = ProductImage
        fields = ['image', 'position']

class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    
    class Meta:
        model = ProductImage
        fields = ['image', 'position']
        
class ProductSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Products
        fields = ['id', 'title', 'description', 'price', 'is_active', 'product_image', 'created_at']