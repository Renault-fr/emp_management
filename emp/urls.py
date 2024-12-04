from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path("alltrucks/", views.all_trucks, name="alltrucks"),
    path("singletruck/<int:empid>/", views.single_truck, name="singletruck"),
    path('singlecompanydetails/<int:empid>/', views.single_truck_company, name="singlecompanydetails"),
    path("addtruck/", views.add_truck, name="addtruck"),
    path('updatespecial/<int:truck_id>/', views.update_special, name="updatespecial"),
    path('updatetruck/<int:truck_id>/', views.update_truck, name="updatetruck"),
    path('deletetruck/<int:truck_id>/', views.delete_truck, name="deletetruck"),
]
