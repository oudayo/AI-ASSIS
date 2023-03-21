from django.urls import path
from .views import upload_audio, index

urlpatterns = [
    path('upload_audio/', upload_audio, name='upload_audio'),
    path('index/', index, name='upload_audio'),

    # Add any other routes here
]
