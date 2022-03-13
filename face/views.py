""" from .models import UserProfile
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import View """
from imaplib import _Authenticator
from .models import UserProfile
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
import face_recognition
import cv2
from django.contrib.auth import authenticate

def facecapture():
    cam = cv2.VideoCapture(0)
    s, img = cam.read()
    if s:
        #while True:
         #   cv2.imshow('Rosto na Camera', img)
          #  if cv2.waitKey(5) == 27:
           #     break
        cv2.imwrite("fotos/filename.jpg",img)
        cam.release()
    
def facedetection(a):

    unknown_image = face_recognition.load_image_file("fotos/filename.jpg")
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]


    known_image = face_recognition.load_image_file(a)  
    know_encoding = face_recognition.face_encodings(known_image)[0]
                     
    results = face_recognition.compare_faces([know_encoding], unknown_encoding)
    return results


def cadastro(request):

    if request.method == 'POST':
        user = request.POST['user']
        photo = request.FILES['photo']
        fr1 = face_recognition.load_image_file(photo)
        fr = face_recognition.face_encodings(fr1)

        if UserProfile.objects.filter(user=user).exists():
            print('Usuario já existente')
            return redirect('cadastro')
        novo = UserProfile.objects.create(user=user, photo=photo, fr=fr)
        novo.save()
        print('CADASTRADO')
        return redirect(reverse_lazy('cadastro'))
    
    return render(request, 'cadastro.html')

def login(request):
    usuarios = UserProfile.objects.all()
    facecapture()

    try:    
        for f in usuarios:
            a = f.photo
            if facedetection(a) == [True]:
                usuario = f.user
                #authenticate(f)
    except:
        usuario = 'Usuario não encontrado'
        
   
        

    #return redirect(reverse_lazy('dashboard', kwargs= {'nome':usuario}))
    return render(request,'login.html', {'usuario':usuario})

def dashboard(request, nome):
    usuario = request.user
    return render(request, 'dashboard.html', {'usuario':usuario})





