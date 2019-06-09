from django.urls import path
from .import views

app_name = "chartApi"

urlpatterns = [
  path('getData1', views.getData1, name='getData1'),
  path('getData2', views.getData2, name='getData2'),
  path('saveToTable2', views.saveToTable2, name='saveToTable2'),
  path('getTable2Data', views.getTable2Data, name='getTable2Data')
]
