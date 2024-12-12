from django.shortcuts import render
from .models import News
from django.core.paginator import Paginator


# Create your views here.
def news(request):
    news_list = News.objects.all().order_by('-date_posted')
    paginator = Paginator(news_list, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'news': page_obj})
