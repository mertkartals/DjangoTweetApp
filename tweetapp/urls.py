from django.urls import path
from . import views

app_name = "tweetapp"

urlpatterns = [
    path('', views.listtweet, name='listtweet'), #atilsamancioglu.com/tweetapp/
    path('addtweet/',views.addtweet, name='addtweet'),  #atilsamancioglu.com/tweetapp/addtweet (yukarıdakini de istersek böyle yazabilirdik)  
    path('addtweetbyform', views.addtweetbyform, name='addtweetbyform'),
    path('addtweetbymodelform', views.AddTweetbyModelForm, name='addtweetbymodelform'),
    path('signup/', views.SignUpView.as_view(), name="signup"),  #sınıflarda son kısma as_view yazarak onu görünüm haline getirmiş oluyoruz.
    path('deletetweet/<int:id>', views.deletetweet, name="deletetweet", )
]