from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy #tembel reverse
from tweetapp.forms import AddTweetForm, AddTweetModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView


# Create your views here.


def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, 'tweetapp/listtweet.html', context=tweet_dict)

@login_required(login_url='/login') #Login_required yazarak giriş yapmayan kullanıcıyı login'e yönlendiriyoruz.
def addtweet(request):
    if request.POST:        #post isteği ise bunu yap
        message = request.POST['message']
        models.Tweet.objects.create(username=request.user,message=message)  #tweetimizi kaydediyoruz.
        return redirect(reverse('tweetapp:listtweet')) #kaydettiğimiz tweetleri listtweete yönlendiriyoruz.
    else:       #post isteği değilse
        return render(request, 'tweetapp/addtweet.html')
    

def addtweetbyform(request):        #Oluşturduğumuz formu işliyoruz. Bu djangonun kendi formudur. 
    if request.method == "POST":    #Eğer post isteği ise post isteğini yazdır.
        form = AddTweetForm(request.POST)
        if form.is_valid():       #Eğer form geçerliyse, temizlenmiş veriyi bize yazdır
            nickname = form.cleaned_data["nickname_input"] 
            message = form.cleaned_data["message_input"]
            models.Tweet.objects.create(nickname=nickname, message=message) 
            return redirect(reverse('tweetapp:listtweet')) 
        else:
            print("error in form!")
            return render(request, 'tweetapp/addtweetbyform.html', context={"form":form})        
    else:
        form = AddTweetForm()
        return render(request, 'tweetapp/addtweetbyform.html', context={"form":form})
    

def AddTweetbyModelForm(request):
    if request.method == "POST":    #Eğer post isteği ise post isteğini yazdır.
        form = AddTweetModelForm(request.POST)
        if form.is_valid():       #Eğer form geçerliyse, temizlenmiş veriyi bize yazdır
            nickname = form.cleaned_data["nickname"] 
            message = form.cleaned_data["message"]
            models.Tweet.objects.create(nickname=nickname, message=message) 
            return redirect(reverse('tweetapp:listtweet')) 
        else:
            print("error in form!")
            return render(request, 'tweetapp/addtweetbymodelform.html', context={"form":form})        
    else:
        form = AddTweetModelForm()
        return render(request, 'tweetapp/addtweetbymodelform.html', context={"form":form})
    
@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:      #requesti yapan kişi gerçekten tweet'i atan kullanıcı ise
        models.Tweet.objects.get(id=id).delete()    #tweet'i silsin
        return redirect('tweetapp:listtweet') #sildikten sonra tweet listesine yönlendir
#Sınıf tabanlı görünüm yapıyoruz.

class SignUpView(CreateView):
    form_class = UserCreationForm   #hangi form. Reverse lazy seçmemizin nedeni görünümün az görünecek olması
    success_url = reverse_lazy('login')  #Kullanıcı başarılı olursa hangi url'ye yönlendirilecek
    template_name = 'registration/signup.html'  #temlate'in adı ne