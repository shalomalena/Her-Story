
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm, ContactForm, VentCommentForm, VentForm
from .models import Category, Post, Vent


def detail(request, category_slug, slug):
    post = get_object_or_404(Post, slug=slug, status=Post.ACTIVE)


    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect('post_detail', slug=slug)
    else:
        form = CommentForm()
    return render (request, 'core/base.html', {'post': post, 'form' : form})

def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(status=Post.ACTIVE)
    return render(request, 'core/base.html', {'category': category, 'posts': posts})

def about(request):
    return render(request, 'core/base.html', {'section': 'about'})

def resources(request):
    return render(request, 'core/base.html', {'section': 'resources'})
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')  # Redirect to a success page or render a success message
    else:
        form = ContactForm()

    return render(request, 'core/base.html', {'contact_form': form})

def contact_success(request):
    return render(request, 'core/base.html')
def vent(request):
    return render(request, 'core/base.html', {'section': 'vent'})


def search(request):
    query = request.GET.get('query', '')

    posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query) | Q(intro__icontains=query) | Q(body__icontains=query))

    return render(request, 'core/base.html', {'posts': posts, 'query': query})

def vent(request):
    
    vent_success = False
    if request.method == 'POST':
        form = VentForm(request.POST)
        if form.is_valid():
            vent = form.save(commit=False)
            vent.approved = False  # Mark as not approved until admin approval
            vent.save()
            return redirect('vent_success')
    else:
        form = VentForm()

    approved_vents = Vent.objects.filter(approved=True).order_by('-created_at')
    return render(request, 'core/base.html', {'vent_form': form, 'vents': approved_vents, 'vent_success': vent_success})

def vent_detail(request, pk):
    vent = get_object_or_404(Vent, pk=pk, approved=True)
    form = VentCommentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        comment = form.save(commit=False)
        comment.vent = vent
        comment.save()
        return redirect('vent_detail', pk=vent.pk)
    return render(request, 'core/base.html', {
        'vent': vent,
        'form': form
    })



def vent_success(request):
    return render(request, 'core/base.html')


