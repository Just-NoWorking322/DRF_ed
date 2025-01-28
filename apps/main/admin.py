from django.contrib import admin
from apps.main.models import Settings, Main, About, Contact, Form
# Register your models here.

@admin.register(Settings)
class SettindsAdmin(admin.ModelAdmin):
    list_display = ('title', )

@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'image', )

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'video', )  

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title','description', 'email', 'adress', 'phone', ) 

@admin.register(Form)
class FormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', ) 
 