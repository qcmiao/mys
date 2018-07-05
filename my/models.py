from django.db import models
        
#服务器
class VirtualMachine(models.Model):
    int_ip = models.CharField(max_length=50)
    ext_ip = models.CharField(max_length=50)
    host_ip = models.CharField(max_length=50)
    vm_name = models.CharField(max_length=50)
    vm_status = models.CharField(max_length=50)
