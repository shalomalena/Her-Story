from django.http import HttpResponse
from django.shortcuts import redirect, render
from vlog.forms import ContactForm
from vlog.models import AboutSection, Category, Post, Contact

def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)
    categories = Category.objects.all()
    return render(request, 'core/base.html', {'posts': posts, 'section': 'frontpage', 'categories': categories})

def about(request):
    about_section = AboutSection.objects.first()
    return render(request, 'core/base.html', {'about_section': about_section, 'about_page': True})

def resources(request):
    return render(request, 'core/base.html', {'section': 'resources'})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'core/base.html', {'form': form})

def contact_success(request):
    return render(request, 'core/base.html')


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")


