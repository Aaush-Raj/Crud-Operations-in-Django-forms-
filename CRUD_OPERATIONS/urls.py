from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('employee/',include('Employee_Register.urls')),
    path('', views.index,name="index"),
    path('bot_search/', views.bot_search,name='bot_search')
    
]
                                   