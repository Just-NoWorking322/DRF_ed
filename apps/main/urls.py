from django.urls import path
from apps.main.views import CreateSettingsView, CreateMainView, CreateAboutView, CreateContactView, CreateFormView

urlpatterns = [
    path("settings/create/", CreateSettingsView.as_view(), name="settings_create"),
    path("main/create/", CreateMainView.as_view(), name="main_create"),
    path("about/create/", CreateAboutView.as_view(), name="about_create"),
    path("contact/create/", CreateContactView.as_view(), name="contact_create"),
    path("form/create/", CreateFormView.as_view(), name="form_create")
]
