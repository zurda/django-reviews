from django.shortcuts import get_object_or_404, render

from .models import Title, Review

def index(request):
    latest_title_list = Title.objects.order_by('-created_at')[:5]
    latest_review_list = Review.objects.order_by('-publish_date')[:5]
    context = {'latest_title_list': latest_title_list, 'latest_review_list': latest_review_list}
    return render(request, 'reviews/index.html', context)

def detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/detail.html', {'review': review})
