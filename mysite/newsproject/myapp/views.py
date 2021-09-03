from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request,'myapp/home.html')
def movie_news(request):
    news1='what is the last hollywood movie?'
    news2 = 'what are the list of last bolywood movies?'
    news3 = 'are you excited about money heist season 5?'
    my_dict={'news1':news1,'news2':news2,'news3':news3}
    return render(request,'myapp/mnews.html',my_dict)
def sports_news(request):
    news1='india defeated from england in 3rd test'
    news2='next test match is on 2nd of sep at OVAL'
    news3='Messi will play for PSG club,paris.'
    my_dict1 = {'news1': news1, 'news2': news2, 'news3': news3}
    return render(request,'myapp/snews.html',my_dict1)

def politics_news(request):
    news1='Afganistan is under Taliban attack'
    news2='America left from Afganistan yesterday'
    news3='india wll airlift indian who stuck in Afganistan by today'
    my_dict3 = {'news1': news1, 'news2': news2, 'news3': news3}
    return render(request, 'myapp/pnews.html', my_dict3)