from django.contrib import admin
from django.contrib.admin.apps import AdminConfig


class CustomAdminSite(admin.AdminSite):
    site_header = 'Easy starter'
    index_title = 'Starter'


class CustomAdminConfig(AdminConfig):
    default_site = 'applications.app.CustomAdminSite'
