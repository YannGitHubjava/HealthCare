from django.shortcuts import render
from django.http import HttpResponse
from .models import Waste
from .forms import WasteForm

def base(request):
    #show_all_waste = Waste.objects.all()
    form = WasteForm()
    return render(request, 'WasteManagement/base.html', {'form':WasteForm})

def all_waste(request):
    show_all_waste = Waste.objects.all()
    print(show_all_waste)
    view_data = {'data': show_all_waste}
    return render(request, 'WasteManagement/all_trash.html', context=view_data)

def add_waste(request):
    trash_name = request.get('trash_name')
    trash_type = request.get('trash_type')
    waste = Waste()
    view_data = {'data': show_all_waste}
    return render(request, 'WasteManagement/all_trash.html', context=view_data)