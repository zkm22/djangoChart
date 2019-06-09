import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import Table1, Table2
import random
from django.forms.models import model_to_dict
from django.core import serializers

@require_http_methods(["GET"])
def getData1(request):
  ''' Data source 1
  '''
  dataList = []
  for i in range(10):
    rand = random.randint(1, 1000)
    dataList.append({
      'area': 'area1',
      'nth': i,
      'value': rand
    })
    Table1.objects.create(
      area = 'area1',
      nth = i,
      value = rand
    )
  try:
    tableItemList = map(
      lambda x:Table1(
        area = x['area'],
        nth = x['nth'],
        value = x['value']
      ), dataList)
    Table1.objects.bulk_create(tableItemList)
    return JsonResponse(dataList, safe=False)
  except Exception as e:
    print(e)
    return JsonResponse({'error': 'error'})

@require_http_methods(["GET"])
def getData2(request):
  ''' Data source 2
  '''
  dataList = []
  for i in range(10):
    rand = random.randint(1, 1000)
    dataList.append({
      'area': 'area2',
      'nth': i,
      'value': rand
    })
    Table1.objects.create(
      area = 'area2',
      nth = i,
      value = rand
    )
  try:
    tableItemList = map(
      lambda x:Table1(
        area = x['area'],
        nth = x['nth'],
        value = x['value']
      ), dataList)
    Table1.objects.bulk_create(tableItemList)
    return JsonResponse(dataList, safe=False)
  except Exception as e:
    print(e)
    return JsonResponse({'error': 'error'})

@require_http_methods(["POST"])
def saveToTable2(request):
  '''Save as local
  '''
  postData = json.loads(request.body)
  try:
    dataList = postData['dataList']
    tableItemList = map(
      lambda x:Table2(
        area1 = x['area1'],
        area2 = x['area2'],
        nth = x['nth']
      ), dataList)
    Table2.objects.bulk_create(tableItemList)
    return JsonResponse({'status': 'success'})
  except Exception as e:
    print(e)
    return JsonResponse({'error': 'error'})

@require_http_methods(["GET"])
def getTable2Data(request):
  '''Get saved data
  '''
  query = Table2.objects.all()[:100]
  dataList = [
    {
      'nth': x.nth if x.nth else 0,
      'area1': x.area1,
      'area2': x.area2,
      'dateTime': x.dateTime.strftime("%Y-%m-%d %H:%M:%S")
    }
    for x in query
  ]
  return JsonResponse(dataList, safe=False)
