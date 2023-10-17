from django.shortcuts import render, redirect
from .models import ShortenedURL
from .forms import URLShortenerForm
import string
import random

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = URLShortenerForm(request.POST)
        if form.is_valid():
            original_url = form.cleaned_data['url']
            # Generate a unique short URL
            while True:
                short_url = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
                if not ShortenedURL.objects.filter(short_url=short_url).exists():
                    break
            # Save the original and short URLs
            shortened_url = ShortenedURL(original_url=original_url, short_url=short_url)
            shortened_url.save()

    # Get the 10 most recent URLs, including both original and shortened URLs
    recent_urls = ShortenedURL.objects.all().order_by('-id')[:10]

    form = URLShortenerForm()  # Create a new form for the template

    # Pass both the form and recent_urls to the template context
    return render(request, 'home.html', {'form': form, 'recent_urls': recent_urls})

def redirect_original_url(request, short_url):
    try:
        shortened_url = ShortenedURL.objects.get(short_url=short_url)
        return redirect(shortened_url.original_url)
    except ShortenedURL.DoesNotExist:
        # Handle cases where the short URL is not found, e.g., show a 404 page.
        return render(request, '404.html', status=404)
    
def error404(request):
    return render(request, '404.html', status=404)

