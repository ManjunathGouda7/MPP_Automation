from django.shortcuts import render

# Create your views here.
def offline_view(request):
    return render(request, 'Automation/Offline.html')
