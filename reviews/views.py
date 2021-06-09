from django.shortcuts import render

from .models import Title

def index(request):
    latest_title_list = Title.objects.order_by('-created_at')[:5]
    context = {'latest_title_list': latest_title_list}
    return render(request, 'reviews/index.html', context)