from django.contrib import admin
from .models import Artiste,Song,Lyric
# Register your models here.
class Adminartiste(admin.ModelAdmin):
    list_display=("id","first_name","last_name","age")
admin.site.register(Artiste,Adminartiste)

class Adminvsong(admin.ModelAdmin):
    list_display=("id","title","date_released","likes","artiste_id")
admin.site.register(Song,Adminvsong)

class Adminlyric(admin.ModelAdmin):
    list_display=("content","song_id")
admin.site.register(Lyric,Adminlyric)