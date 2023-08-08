from django.shortcuts import render

posts = [
    {
        'author' : 'Shwe Gyi',
        'title' : 'The Art of Not F**king Care',
        'content' : 'First post content',
        'date_posted' : 'August 7, 2023',

    },
     {
        'author' : 'Wai Gyi',
        'title' : 'Gone with The Wind',
        'content' : 'second post content',
        'date_posted' : 'July 7, 2023',

    },
     {
        'author' : 'Pon Gyi',
        'title' : 'The Hope Of Myanmar(Burma)',
        'content' : 'Third post content',
        'date_posted' : 'April 7, 2023',

    }
]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'} )