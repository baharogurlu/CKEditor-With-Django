from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from .forms import PostForm
from .models import Post

# Create your views here.



def index(request):
    return render(request, 'ck_editor/index.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'ck_editor/post_list.html', {'posts': posts})


def save_post_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            posts = Post.objects.all()
            data['html_post_list'] = render_to_string('ck_editor/includes/partial_post_list.html', {
                'posts': posts
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}

    data['html_form'] = render_to_string(template_name, context, request=request)
    data['form_fields'] = list(PostForm.base_fields.keys())


    return JsonResponse(data)


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
    else:
        form = PostForm()
    return save_post_form(request, form, 'ck_editor/includes/partial_post_create.html')


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
    else:
        form = PostForm(instance=post)
    return save_post_form(request, form, 'ck_editor/includes/partial_post_update.html')


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    data = dict()
    if request.method == 'POST':
        post.delete()
        data['form_is_valid'] = True
        posts = Post.objects.all()
        data['html_post_list'] = render_to_string('ck_editor/includes/partial_post_list.html', {
            'posts': posts
        })
    else:
        context = {'post': post}
        data['html_form'] = render_to_string('ck_editor/includes/partial_post_delete.html', context, request=request)

    return JsonResponse(data)
