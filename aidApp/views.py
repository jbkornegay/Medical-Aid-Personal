from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from .forms import FeedbackForm
from .models import Comment, Post, Support
from django.views.generic import CreateView
    

# Create your views here.
def index(request):
    return HttpResponse("<h1>Medical Aid app Homepage</h1>")

def feedbackview(request):
    form= FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'feedback/feedback.html', context)

class CommentView(SuccessMessageMixin, CreateView):
    model = Comment
    template_name = 'aidApp/feedback_form.html'
    fields = ['full_name', 'email', 'message']
    success_url = '/aid/comment'
    success_message = 'Comment Created!'
    


@login_required
def createpost(request):
    if request.method == "POST":
        if request.POST.get('title') and request.POST.get('content'):
            post = Post()
            post.title= request.POST.get('title')
            post.content= request.POST.get('content')
            post.save()
            messages.success(request, f'Post submitted succesfully!')
            return render(request, 'aidApp/createpost.html')
    else:
        return render(request, 'aidApp/createpost.html')

def support_view(request):
    if request.method == "POST":
        if request.POST.get('fullname') and request.POST.get('message'):
            support = Support()
            support.fullname= request.POST.get('fullname')
            support.email= request.POST.get('email')
            support.complaint= request.POST.get('complaint')
            support.message= request.POST.get('message')
            support.save()
            return redirect('support-success')
    else:
        return render(request, 'aidApp/patient/patient-support.html')



def support_success_view(request):
    return render(request, 'aidApp/patient/patient-support-feedback.html')
