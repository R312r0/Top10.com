from django.shortcuts import render, redirect
from .models import *
from django.http import Http404, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from templates.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaulttags import register


# Create your views here.

def index(request):
    output = Post.objects.order_by('?')[0]
    posts = Post.objects.all()
    return render(request, '../templates/index.html', {'output': output, 'posts': posts})


def tech(request):
    output = Post.objects.filter(category__category_name="Tech")
    category = Category.objects.filter(category_title="Top 10 Technical top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def finance(request):
    output = Post.objects.filter(category__category_name="Finance")
    category = Category.objects.filter(category_title="Top 10 Finance top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def health(request):
    output = Post.objects.filter(category__category_name="Health")
    category = Category.objects.filter(category_title="Top 10 Health top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def lifestyle(request):
    output = Post.objects.filter(category__category_name="Lifestyle")
    category = Category.objects.filter(category_title="Top 10 Lifestyle top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def family(request):
    output = Post.objects.filter(category__category_name="Family")
    category = Category.objects.filter(category_title="Top 10 Family top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def business(request):
    output = Post.objects.filter(category__category_name="Business")
    category = Category.objects.filter(category_title="Top 10 Business top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def shopping(request):
    output = Post.objects.filter(category__category_name="Shopping")
    category = Category.objects.filter(category_title="Top 10 Shopping top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def entertainment(request):
    output = Post.objects.filter(category__category_name="Entertainment")
    category = Category.objects.filter(category_title="Top 10 Entertainment top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def personal_growth(request):
    output = Post.objects.filter(category__category_name="PersonalGrowth")
    category = Category.objects.filter(category_title="Top 10 PersonalGrowth top's:")
    return render(request, '../templates/tech.html', {'output': output, 'category': category})


def detail(request, post_slug):
    main_post = Post.objects.get(slug=post_slug)
    try:
        output = PostItem.objects.filter(subject__subject=main_post.subject).order_by('place_in_top')
    except:
        raise Http404("Post dont found")


    comments = Comment.objects.filter(post__subject=main_post.subject).order_by('-id')[:10]
    comments_count = comments.count()

    return render(request, '../templates/detail.html', {'main_post':main_post, 'output': output,  'comments': comments, 'post_slug':post_slug,'comments_count': comments_count,})


def leave_comment(request, post_slug):
    try:
        output = Post.objects.get(slug=post_slug)
    except:
        raise Http404("Post dont found")

    user = request.user

    output.comment_set.create(user_name=user, comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('top10:detail', args=(post_slug,)))

@register.filter
def organize_posts(arr):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(arr) - 1):
            if arr[i].place_in_top > arr[i + 1].place_in_top:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True



def registerPage(request):
    form = CreateUserForm

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('top10:log-in')

    context = {'form': form}

    return render(request, '../templates/register.html', context)


def logIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('top10:index')
        else:
            messages.info(request, 'Username or password is incorrect')

    return render(request, '../templates/login.html')


def logOut(request):
    logout(request)

    return redirect('top10:log-in')
