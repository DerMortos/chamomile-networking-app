from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class SignUpView(View):
    def get(self, request):
        return HttpResponse("signup stub")
def feed(request):
    return HttpResponse("feed stub")

def profile(request, username):
    return HttpResponse("profile stub")

def toggle_follow(request, username):
    return HttpResponse("follow stub")

def member_list(request):
    return HttpResponse("members stub")

def post_detail(request,  pk):
    return HttpResponse("post stub")

def edit_profile(request):
    return HttpResponse("edit profile stub")

def delete_message(request, pk):
    return HttpResponse("delete message stub")