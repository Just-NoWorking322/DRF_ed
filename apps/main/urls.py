from django.urls import path
from apps.main.views import (CreateSettingsView, CreateMainView, CreateAboutView, 
                             CreateContactView, CreateFormView, ProductCreateView, 
                             ProductListView, ProductDeleteView, ProductUpdateView)

urlpatterns = [
    path("settings/create/", CreateSettingsView.as_view(), name="settings_create"),
    path("main/create/", CreateMainView.as_view(), name="main_create"),
    path("about/create/", CreateAboutView.as_view(), name="about_create"),
    path("contact/create/", CreateContactView.as_view(), name="contact_create"),
    path("form/create/", CreateFormView.as_view(), name="form_create"),
    path("product/create/", ProductCreateView.as_view(), name="product_create"),
    path("product/list/", ProductListView.as_view(), name="product_list"),
    path("product/<int:pk>/delete/", ProductDeleteView.as_view(), name="product_delete"),
    path("product/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
]
