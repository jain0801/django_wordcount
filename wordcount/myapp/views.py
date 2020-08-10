from django.shortcuts import render,get_object_or_404, redirect
from .models import Word

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext']
    words=text.split()
    word_dic={}
    for word in words:
        if word in word_dic:
            word_dic[word]+=1
        else:
            word_dic[word]=1
    return render(request, 'result.html', {'full':text, 'total':len(words), 'dic':word_dic.items()})

# def detail(request, result_id):
#     detail = get_object_or_404(Word, pk=result_id)
#     return render(request, 'result.html', {'detail': detail})

def create(request):
    word_result=Word()
    word_result.wordcount=request.GET['result']
    word_result.save()
    return redirect(str(word_result.id))

# def post_add(request):
#     if request.method=='POST':
#         User = get_user_model()
#         author = User.objects.get(username='jain0801')
#         word_result=request.POST['fulltext']
#         post=Post.objects.create(
#             fulltext=fulltext,
#         )
#         post.publish()
#         return HttpResponse('POST method')