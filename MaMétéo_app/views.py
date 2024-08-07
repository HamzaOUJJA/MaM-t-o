from django.shortcuts import render
from django.contrib import messages
from googletrans import Translator
import requests
import datetime


def home(request):
     try:
          ville = request.POST['ville'] 
     
          url = f'https://api.openweathermap.org/data/2.5/weather?q={ville}&appid=6a1858373170036b7d59fd4bbe98cae2'
          Paramètre = {'units':'metric'}

          translator = Translator()

          Info = requests.get(url,params=Paramètre).json()
          description_En = Info['weather'][0]['description']
          icon = Info['weather'][0]['icon']
          temp = Info['main']['temp']
          Jour = datetime.date.today()
          print(description_En)
          description = translator.translate(description_En, src='en', dest='fr').text
          

          return render(request,'MaMétéo_app/index.html' , 
                        {'description':description , 
                         'icon':icon ,
                         'temp':temp , 
                         'Jour':Jour , 
                         'ville':ville ,
                         'image_url': f"https://weather-application-image.netlify.app/videos/{description_En}.png", 
                         'exception_occurred':False })
    
     except KeyError:
          exception_occurred = True
          messages.error(request,'Entered data is not available to API')   
          
          Jour = datetime.date.today()

          return render(request,'MaMétéo_app/index.html' ,
                        {'description':'clear sky', 
                         'icon':'01d',  
                         'temp':25, 
                         'Jour':Jour, 
                         'ville':'Paris', 
                         'image_url': f"https://weather-application-image.netlify.app/videos/default.png",
                         'exception_occurred':exception_occurred } )
               
    
    