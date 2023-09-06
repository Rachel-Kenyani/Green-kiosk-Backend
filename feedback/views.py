from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'feedback/review_list.html', {'reviews': reviews})

def review_detail(request, id):
    review = Review.objects.get(id=id)
    return render(request, 'feedback/review_detail.html', {'review': review})

def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

def review_update(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save()
            return redirect('feedback/review_detail, id=id')
    else:
        form = ReviewForm(instance=review)
    return render(request, 'feedback/review_update.html', {'form': form})

