from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="nickname", max_length=50)
    message_input = forms.CharField(label="message", max_length=100,
                                  widget=forms.Textarea(attrs={'class':'tweetmessage'}))   
    
    #text area ile formumuzdaki message kısmının alanını büyütüyoruz.
    #içinde sınıf oluşturarak message kısmını da özelleştirebiliyoruz.

class AddTweetModelForm(ModelForm):
    class Meta:         #meta bilgisi
        model = Tweet    #modelimizi import etmiştik
        fields = ['username', 'message']
        

    