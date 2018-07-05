from django.shortcuts import render
from django.http import HttpResponse
from my.models import VirtualMachine
from .vm_ctl import destroy_vm
from .vm_ctl import start_vm
from .vm_ctl import reboot_vm
from .vm_ctl import suspend_vm
def vmviewer(request):
    vm_info=VirtualMachine.objects.all()
    context = {'vm_info': vm_info}
    return render(request, 'index.html', context)

def suspend(request):
#    vmname=request.POST.get('vmname')
#    suspend_vm(vmname)
    suspend_vm()
    return HttpResponse('success')
