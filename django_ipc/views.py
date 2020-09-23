from django.shortcuts import render
import os
import subprocess


# Create your views here.
def home(request):

    # subprocess.Popen(['/home/adminp/bfl/projects/django_ipc/django_ipc/scratch.sh'], shell=True)
    # os.system('python /home/adminp/bfl/projects/django_ipc/django_ipc/camera.py')
    # os.system('python /home/adminp/bfl/projects/django_ipc/ipc_files/ods.py')
    return render(request, 'home_page.html', {'posts': "ANKIT SUWAL"})
