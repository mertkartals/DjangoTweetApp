from django.contrib import admin
from tweetapp.models import Tweet  #ya da from . import models da yazabiliriz.

# Register your models here.

class TweetAdmin(admin.ModelAdmin):
    fieldsets =[                 #alan setleri 
        ('Message Group',{"fields":["message"]}), 
        ('Nickname Group',{"fields":["nickname"]})
    ]


    #fields = ['message', 'nickname'] #Bunu yaparak admin sayfamızı düzenliyoruz. Örneğin ilk mesaj altta ise takma ad yer alır


admin.site.register(Tweet, TweetAdmin)  #kaydettiğimiz tweet'i admin sitesine kaydeder ve oradan görebiliriz. Tweetadmin'i sonradan ekledik.

