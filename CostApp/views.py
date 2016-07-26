from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
# Create your views here.
from django.views.generic import TemplateView



def Add(request):
    return JsonResponse(request.POST)
    #return HttpResponse(request)


class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'CostApp/index.html')



