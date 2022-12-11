from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views.generic import (
    View,
    ListView,
    UpdateView,
    DeleteView)
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import loader
from .models import Post, Comment
from .forms import CommentForm, BlogPostForm
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError


class PostList(ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        form = CommentForm(data=request.POST)
        if  form.is_valid():
            form = form.save(commit=False)
            form.name = self.request.user
            form.email = request.user.email
            form.post = post
            form.save()
        else:
            form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "form": form,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def form_valid(self, form):
        """ validate form and connect to user """
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CommentUpdateView(UpdateView):
    """ Update comments via update_post.html """
    model = Comment
    form_class = CommentForm
    context_object_name = 'comment'
    template_name = 'update_post.html'

    def form_valid(self, form):
        """
        Success url return to blogpost in question
        with successfull commentform
        """
        self.success_url = f'/{self.get_object().post.slug}/'
        return super().form_valid(form)


class CommentDeleteView(DeleteView):
    """ Connects comment to DeleteView function """
    model = Comment
    template_name = 'delete_comment_post.html'
    context_object_name = 'comment'

    def get_success_url(self, *args):
        """ Success url return to blogpost in question """
        self.success_url = f'/{self.get_object().post.slug}'
        self.slug = self.get_object().post.slug
        return reverse_lazy('post_detail', args=[self.slug])


class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def create_post(request):
    """
    Allow an admin user to create a Blog Post
    """
    if request.user:

        if request.method == 'POST':
            form = BlogPostForm(request.POST, request.FILES)
            if form.is_valid():
                blog_post = form.save(commit=False)
                blog_post.author = request.user
                blog_post.save()
                messages.info(request, 'Blog Pending Approval!')
                return redirect('/')
            else:
                messages.error(request, 'Please check the form for errors. \
                    Blog failed to add.')
        else:
            form = BlogPostForm()
    else:
        messages.error(
            request, 'Sorry, you do not have permission to do that.')
        return redirect(reverse('home'))

    template = 'new_post.html'

    context = {
        'form': form,
    }
    return render(request, template, context)


# @login_required
# def edit_blog(request, blog_post_id):
#     """
#     Allow all users to edit the blogs they created
#     """
#     if request.user:

#         blog_post = get_object_or_404(Post, pk=blog_post_id)

#         if request.method == 'POST':
#             form = PostForm(request.POST, request.FILES, instance=blog_post)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, 'Blog post updated successfully!')
#                 return redirect('blog')
#             else:
#                 messages.error(request, 'Please check the form for errors. \
#                     Blog post failed to update.')
#         else:
#             form = PostForm(instance=blog_post)
#             messages.info(request, f'Editing {blog_post.title}')
#     else:
#         messages.error(request, 'Sorry, you do not have permission for that.')
#         return redirect(reverse('home'))

#     template = 'edit_blog.html'

#     context = {
#         'form': form,
#         'blog_post': blog_post,
#     }

#     return render(request, template, context)


@login_required
def delete_post(request, blog_post_id):
    """User can delete their own blog post"""
    if request.method == "POST":
        blog_post = get_object_or_404(Post, pk=blog_post_id)
        blog_post.delete()
    else:
        return render(request, 'delete_blog.html')
    messages.success(request, 'The blog has been deleted successfully!')

    return redirect('/')


def contact(request):
    if request.method == 'POST':
        contact = contact(request.POST)
        if form.is_valid():
            form.save()
        body = {
                'first_name': form.data['first_name'],
                'last_name': form.data['last_name'],
                'email': form.data['email_address'],
                'body': form.data['body'], 
                }
                
    form = ContactForm()
    return render(request, 'contact.html', {'form': form})