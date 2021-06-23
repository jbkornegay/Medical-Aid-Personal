from django.shortcuts import render
from django.http import HttpResponse
from .forms import FeedbackForm

# Create your views here.
def index(request):
    return HttpResponse("<h1>Medical Aid app Homepage</h1>")

def feedbackview(request):
    form= FeedbackForm(request.POST or None)
    if form.is_valid():
        form.save()
  
    context= {'form': form }
        
    return render(request, 'feedback/feedback.html', context)
