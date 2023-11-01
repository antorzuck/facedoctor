from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests


# Create your views here.
def home(r):
   return render(r,'index.html')
@csrf_exempt
def get_face(r):
    if r.method == 'POST':
      print("success")
      xxx = r.FILES.get('selfie')
      try:
        url = "http://apifacex.pythonanywhere.com/"
        files = {'selfie': r.FILES.get('selfie')}
        res = requests.post(url, files=files).json()
        print(res['count'])
        print(res['result'])
        return JsonResponse({"shape":res['face_shape'],'result':res['result']})
      except Exception as e:
        return JsonResponse({"shape":str(e)})
