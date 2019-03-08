
from django.contrib import admin
from django.urls import path, include
import schedule.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schedule.views.home, name='home'),
    path('schedule/', include('schedule.urls')),

]
