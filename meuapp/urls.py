from django.urls import path
from . import views

urlpatterns = [
    path('consulta/', views.home, name='consulta'),
    path('your-name/', views.get_name, name='get_name'),
    path('thanks/', views.thanks, name='thanks'),  # Você precisará criar esta view
]
