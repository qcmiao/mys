from django.shortcuts import render
from django.http import HttpResponse
from my.models import VirtualMachine

def vmviewer(request):
    vm_info=VirtualMachine.objects.all()
    context = {'vm_info': vm_info}
    return render(request, 'index.html', context)
