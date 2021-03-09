from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect,reverse,get_object_or_404
from posts.models import PostModel
from posts.forms import  CommentForm
from django.views.generic import *
"""def HomeView(request):
    section="home"
    return render(request,'home.html',{'section':section})"""


def PostDetial(request, post_id):
    p = get_object_or_404(PostModel, id=post_id)
    comments = p.comment.all()
    new_com = None

    if request.method == 'POST':
        c_form = CommentForm(data=request.POST)

        if c_form.is_valid():
            new_com = c_form.save(commit=False)
            new_com.posted_by = request.user
            new_com.post = p
            new_com.save()



    else:
        c_form = CommentForm()

    return render(request, 'postmodel_detail.html',
                  {'post': p, 'comments': comments, "form": c_form, 'new': new_com
                   })

class HomeView(ListView):
    model=PostModel
    queryset = PostModel.objects.all()
    #context_object_name
    paginate_by = 3
    template_name = 'home.html'

