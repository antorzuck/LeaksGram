from django.shortcuts import render
from django.http import HttpResponse

def firebase_messaging_sw(request):
 
    #firebase_config =  



    script_content = """
    importScripts('https://www.gstatic.com/firebasejs/10.12.3/firebase-app.js');
    importScripts('https://www.gstatic.com/firebasejs/10.12.3/firebase-messaging.js');


    const firebaseConfig = {
    apiKey: "AIzaSyBeA5Vt0Lc5Hbe0i_dXJSLWLiG0FGq0s44",
    authDomain: "leaksgram-4cc3b.firebaseapp.com",
    projectId: "leaksgram-4cc3b",
    storageBucket: "leaksgram-4cc3b.appspot.com",
    messagingSenderId: "1003081775172",
    appId: "1:1003081775172:web:c58c7f451b2a2327c4a411",
    measurementId: "G-P6DEK2T2MV"
  };

    firebase.initializeApp(firebaseConfig);


    const messaging = firebase.messaging();

    messaging.onBackgroundMessage(function(payload) {{
      console.log('Received background message ', payload);

   
      const notificationTitle = payload.notification.title;
      const notificationOptions = {{
        body: payload.notification.body,
        icon: '/firebase-logo.png'
      }};

      self.registration.showNotification(notificationTitle, notificationOptions);
    }});
    """

    # Return as JavaScript content
    response = HttpResponse(script_content, content_type='application/javascript')
    return response



def home(request):
    return render(request, 'home.html')


def video(request):
    return render(request, 'video.html')


