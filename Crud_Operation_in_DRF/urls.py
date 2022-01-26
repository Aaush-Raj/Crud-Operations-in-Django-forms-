from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD:Crud_Operation_in_DRF/urls.py
    path('employee/',include('Employee_Register.urls')),
=======
    #path('employee/',include('Employee_Register.urls')),
    path('', views.index,name="index"),
    path('bot_search/', views.bot_search,name='bot_search')
>>>>>>> 025d08cf87c86531b15214baca5aa7ce0cb4360c:CRUD_OPERATIONS/urls.py
    
]
                                   
