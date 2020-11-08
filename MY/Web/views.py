from django.shortcuts import render, redirect
from .models import book, comments
from django.http import HttpResponse
from datetime import date, timedelta
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.models import User
from .forms import AuthUserForm, RegisterUserForm, Create_book, Add_comment
from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
import operator
id_me=0

# Create your views here.
def Main(request):
    all_books = book.objects.all
    return render(request, 'Web/Main.html', {'books':all_books})

def News(request):
    all_books = book.objects.all
    old_data = date.today()-timedelta(7)
    return render (request, 'Web/new.html', {'books':all_books, 'old_data':old_data})

def About(request):
    return render (request, 'Web/about.html')

def book_id(request, book_id, id=0):
    global id_me
    id_me=book_id
    id=0
    try:
        book_now = book.objects.get(id=book_id)
    except:
        return HttpResponse(status= 404)
    comment= comments.objects.all

    return render(request, "Web/Book_id.html", {'book':book_now, 'comments':comment})
    

def By_novelty(request):
    book_novely = book.objects.order_by("-date_added")
    return render(request, "Web/book_novelty.html", {'book_novely':book_novely})

def By_author(request):
    book_author = book.objects.all
    l=[]
    for b in book_author():
        if b.author not in l:
            l.append(b)
    return render(request, "Web/book_author.html", {'l':l, "books":book_author })

def id_author(request, author):
    author_all = book.objects.all
    return render(request, "Web/Author_id.html", {'author':author,"book_all":author_all })

class book_loginView(LoginView):
    template_name = 'Web/Auth.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('Main')
    def get_success_url(self):
        return self.success_url

class book_userView(CreateView):
    model = User
    template_name = 'Web/Create_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('Main')
    success_msg = 'Пользователь успешно создан'
    def form_valid(self, form):
        form_valid = super().form_valid(form)
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        auth_user = authenticate(username=username, password=password)
        login(self.request, auth_user )
        return form_valid

class book_logOut(LogoutView):
    next_page = reverse_lazy('Main')

class add_book(CreateView):
    model = book
    template_name = "Web/New_book.html"
    form_class = Create_book
    success_url = reverse_lazy('Main')


def add_comment(request):
    
    form = Add_comment()
    global id_me
    

    if request.method == "POST":
        form = Add_comment(request.POST)
        if form.is_valid():
            post_entry = comments()
            post_entry.name = form.cleaned_data['name']
            post_entry.comment = form.cleaned_data['comment']
            post_entry.score = form.cleaned_data['score']
            post_entry.book_id = form.cleaned_data['book_id']
            post_entry.save()
            return redirect('Main')
    else:
        form = Add_comment()
    return render(request , 'Web/Create_comment.html' , {"form":form,'f':id_me })

def By_comments(request):
    book_comments = comments.objects.all
    book_com = book.objects.all
    h={}
    for b in book_comments():
        if b.book_id not in h:
            h[b.book_id]=1
        else:
            h[b.book_id]+=1

    sorted_by_value = sorted(h.items(), key=lambda kv: -kv[1])
    sorted_by_value
    h=dict(sorted_by_value)
        
    return render(request, "Web/book_comments.html", {'h':h, "books":book_com })