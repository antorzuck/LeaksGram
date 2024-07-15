importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.1/firebase-messaging.js');


firebase.initializeApp({
    apiKey: "AIzaSyBeA5Vt0Lc5Hbe0i_dXJSLWLiG0FGq0s44",
    authDomain: "leaksgram-4cc3b.firebaseapp.com",
    projectId: "leaksgram-4cc3b",
    storageBucket: "leaksgram-4cc3b.appspot.com",
    messagingSenderId: "1003081775172",
    appId: "1:1003081775172:web:c58c7f451b2a2327c4a411",
    measurementId: "G-P6DEK2T2MV"
  });


const messaging = firebase.messaging();

messaging.onBackgroundMessage((payload) => {
    console.log(
      '[firebase-messaging-sw.js] Received background message ',
      payload
    );
   
    const notificationTitle = 'Background Message Title';
    const notificationOptions = {
      body: payload.notification.body,
      icon: 'https://api.dicebear.com/9.x/icons/svg?seed=Kitty',
    };
  
    self.registration.showNotification(notificationTitle, notificationOptions);
  });
  
