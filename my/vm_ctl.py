#!/usr/bin/env python
#coding=utf-8
import os
import libvirt
import sys



#dom0.info()[0]==1 runing  ==3  paused   ==5  shutdown
def destroy_vm(host_ip,vmname):
    host_ssh='qemu+ssh://root@{}/system'.format(host_ip)
    conn = libvirt.open(host_ssh)
    dom0 = conn.lookupByName(vmname)
    if dom0.info()[0]==1 or dom0.info()[0]==3:
        dom0.destroy()
    else:
        pass


def start_vm(host_ip,vmname):
    host_ssh='qemu+ssh://root@{}/system'.format(host_ip)
    conn = libvirt.open(host_ssh)
    dom0 = conn.lookupByName("template")
    if dom0.info()[0]==5:
        dom0.create()
    else:
        pass

def reboot_vm(host_ip,vmname):
    host_ssh='qemu+ssh://root@{}/system'.format(host_ip)
    conn = libvirt.open(host_ssh)
    dom0 = conn.lookupByName(vmname)
    if dom0.info()[0]==1:
        dom0.reboot()
    else:
        pass

#def suspend_vm(host_ip,vmname):
def suspend_vm():
#    host_ssh='qemu+ssh://root@{}/system'.format(host_ip)
    host_ssh='qemu+ssh://root@30.207.39.18/system'
    conn = libvirt.open(host_ssh)
#    dom0 = conn.lookupByName(vmname)
    dom0 = conn.lookupByName("template")
    if dom0.info()[0]==1:
       dom0.suspend()
    elif dom0.info()[0]==3:
       dom0.resume()
    else:
       pass

if __name__ == '__main__':
    suspend_vm('1.template')
