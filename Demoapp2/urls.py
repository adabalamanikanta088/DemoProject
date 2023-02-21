from django.urls import path;	#new
from Demoapp2 import views;

urlpatterns = [
	path('third/', views.f3),
	path('fourth/', views.f4),
];
