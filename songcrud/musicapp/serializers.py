from rest_framework import serializers
from .models import Artiste,Song

class ArtisteSerializers(serializers.ModelSerializer):
    class Meta:
        model=Artiste
        # fields=['id','first_name','last_name','age']
        fields="__all__"
        
class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model=Song
        # fields=['id','title','date_released','likes','artiste_id']
        fields="__all__"