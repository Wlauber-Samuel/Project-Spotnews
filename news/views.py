from django.shortcuts import render, redirect
from news.models import News, Category
from news.forms import CreateNewsForm


# Create your views here.
def home(request):
    context = {"news": News.objects.all()}
    return render(request, "home.html", context)


def news_details(request, news_id):
    context = {"news": News.objects.get(id=news_id)}
    return render(request, "news_details.html", context)


def news_forms(request):
    forms = CreateNewsForm()
    if request.method == "POST":
        forms = CreateNewsForm(request.POST)
        if forms.is_valid():
            Category.objects.create(**forms.cleaned_data)
            return redirect("home-page")
    context = {"forms": forms}
    return render(request, 'categories_form.html', context)
