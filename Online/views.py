from django.shortcuts import render

# Create your views here.
def online_view(request):
    return render(request, 'Automation/Online.html')