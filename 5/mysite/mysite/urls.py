
from django.contrib import admin
from django.urls import path
from app.views import home, retrieve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('retrieve/<int:id>', retrieve)
]
