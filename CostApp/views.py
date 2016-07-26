from django.db.models import Model
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.http import JsonResponse
# Create your views here.
from django.views.generic import TemplateView

from CostApp.models import Group , Cost
from django.utils import timezone

def Add(request):
    group = Group.objects.get(name=request.POST['group'])
    group.save()
    cost=Cost(name=request.POST['name'],group=group,price=request.POST['cost'],priority=request.POST['priority'],date=timezone.now(),user=request.POST['user'])
    cost.save()
    return HttpResponse(group.name)



class Index(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'CostApp/index.html')



