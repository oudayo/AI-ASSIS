from django.shortcuts import render

import os
from django.conf import settings
from django.http import HttpResponseBadRequest, HttpResponse
from django.core.files.storage import FileSystemStorage

from . import assistant

import base64
import json
from django.conf import settings




def upload_audio(request):
    if request.method == 'POST' and request.FILES.get('audio'):

        #delete the old audio files 
        try:
            os.remove(str(settings.BASE_DIR).replace('\\', '/') + '/media/audio/output.wav')
            os.remove(str(settings.BASE_DIR).replace('\\', '/') + '/media/audio/r.mp3')
            os.remove(str(settings.BASE_DIR).replace('\\', '/') + '/media/audio/audio_model.mp3')
        except FileNotFoundError:
            print('file not found')
            


        



        #get the audio file 
        audio_file = request.FILES['audio']
        fs = FileSystemStorage()
        
        # Save the file to a specific directory on the server
        filename = fs.save('audio/' + audio_file.name, audio_file)
        file_url = fs.url(filename)


        # file_url = 'C:/Users/khalil/Documents/ouday/projet/' + file_url
        file_url = str(settings.BASE_DIR).replace('\\', '/') + file_url

        #pass the audio file to the ai and generate the ai response 
        link = assistant.respond(file_url)

        # sending the bot's response
        audio_path = str(settings.BASE_DIR).replace('\\', '/') + '/media/audio/audio_model.mp3'
        
        with open(audio_path, 'rb') as file:
            encoded_audio_data = base64.b64encode(file.read()).decode('utf-8')
            response_data = {
            'link': link,
            'audio': encoded_audio_data
        }
            response_json = json.dumps(response_data)
            response = HttpResponse(response_json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="song.mp3"'
            return response
    else:
        return HttpResponseBadRequest('Invalid request')




def index(request):
    
    return render(request, 'index.html')