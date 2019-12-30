from django.shortcuts import render
from .models import User
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    users_list = User.objects.all() 
    page = request.GET.get('page', 1)
    paginator = Paginator(users_list, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users= paginator.page(paginator.num_pages)
    context= {'users':users }
    return render(request, 'users/index.htm', context)


def detail(request, user_id):
    users = User.objects.get(pk=user_id)
    context= {'users':users }
    return render(request, 'users/detail.htm', context)