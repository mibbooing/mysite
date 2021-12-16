from django.shortcuts import render

# Create your views here.
# ----------------------[edit]---------------------- #
from django.http import HttpResponse

def index(requst):
    return HttpResponse("안녕하세요 pybo에 오신것을 환영합니다.")
# ----------------------[edit]---------------------- #