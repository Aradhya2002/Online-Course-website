from django.shortcuts import render, redirect
from home.models import saveregister, video, teacher
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import cv2
import threading
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
from .forms import Video_form
from django.shortcuts import HttpResponse
import razorpay

def Home(request):
    return render(request, 'index.html')

def Saveinfo(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        password=request.POST.get('password')
        en = saveregister(name=name, email=email, number=number, password=password)
        en.save()
    return render(request, 'index.html')

def Login(request):
    if request.method == "POST":
        name=request.POST.get('name')
        password=request.POST.get('password')
        
        user = authenticate(request, name=name, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'dashboard.html')
    

def Logout(request):
    logout(request)
    return render(request, 'index.html')

@gzip.gzip_page
def main(request):
    context = {}
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'main.html', context=context)

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def admin(request):
    return render(request, 'upload.html')

def index(request):
    Video=video.objects.all()
    return render(request, 'upload.html', {"video":Video})

def teacher(request):
    if request.method == "POST":
        name=request.POST.get('tname')
        password=request.POST.get('tpassword')
        
        user = authenticate(request, name=name, password=password)
        if user is not None:
            login(request, user)
    return render(request, 'teacher.html')

def Saveinfo_teacher(request):
    if request.method == "POST":
        name=request.POST.get('tname')
        email=request.POST.get('temail')
        number=request.POST.get('tnumber')
        password=request.POST.get('tpassword')
        en = teacher(name=name, email=email, number=number, password=password)
        en.save()
    return render(request, 'index.html')


def showvideo(request):

    lastvideo= video.object.last()

    video= lastvideo.video


    form= Video_form(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()

    
    context= {'video': video,
              'form': form
              }
    
      
    return render(request, 'videos.html', context)

def aasd(request):
    return render(request, 'videos.html')

def Pay(request):
    if request.method == "POST":
        amount = 50000
        order_currency = 'INR'
        client = razorpay.Client(
            auth=("rzp_test_HOyG51ehWWEYhb" , "43xIavtFKNCYadgiBOI92rUC"))

        payment = client.order.create({'amount':amount, 'currency':'INR', 'payment_capture':'1'})
    return render(request, 'pay.html')
