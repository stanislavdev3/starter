from django.contrib import admin
from django.urls import path

from applications.core.views import main_page_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page_view),
]
