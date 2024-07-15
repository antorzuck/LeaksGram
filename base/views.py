from django.shortcuts import render
from django.http import HttpResponse
import firebase_admin
from firebase_admin import credentials
from firebase_admin import messaging

def send_push_notification(device_token):
    cred_path = '/data/data/com.termux/files/home/leaksgram/base/leaksgram-4cc3b-firebase-adminsdk-k47u1-23b3c7f01f.json'

    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred)
    print(cred, "creeeeeeeeeeeeeed")
    message = messaging.Message(
        notification=messaging.Notification(
            title='Test Notification',
            body='This is a test notification',
        ),
        token=device_token,
    )

 
    response = messaging.send(message)
    print('Successfully sent message:', response)

device_token = 'cs9oIdP6n88iI4NmwVgNGW:APA91bH7DVDnxmaeVqCvKBmfxhP8uqNTymY5sDG4XeeAj8WrDxbt-ZnjX3FxxWqmHLsWFQyWS8rAzBVqyiK0s1sWcRYI-x-v7mYFjGTAvQj6XDbYwmPaRhdXSr1pf25moqmYoHWBSVxr'

#send_push_notification(device_token)



def home(request):
    token = request.GET.get('token')
    print(token)
    send_push_notification(device_token)
    return render(request, 'home.html')


def video(request):
    return render(request, 'video.html')


