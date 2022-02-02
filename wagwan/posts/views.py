from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import generic
from django.shortcuts import render, redirect
from shapeshifter.views import MultiFormView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from . import forms
from . import models

# POSTS VIEWS


# ------------------------POST  VIEWS ------------------------------#

class PostCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.PostForm
    template_name = 'posts/post_form.html'

    def form_valid(self, form):
        """ function will set the author name automatically to the
        user logged in when post.author is passed inside the template """

        form.instance.author = self.request.user
        return super().form_valid(form)


class PostListView(LoginRequiredMixin, generic.ListView):
    model = models.Post
    paginate_by = 7


class UserPostListView(LoginRequiredMixin, generic.ListView):
    """ class will display posts from the selected user """
    model = models.Post
    template_name = 'posts/user_post.html'
    paginate_by = 7

    def get_queryset(self):
        """ self.kwargs.get method will get the username form the URL
        - see the url for this class """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return models.Post.objects.filter(author=user)


class CategoryPostListView(LoginRequiredMixin, generic.ListView):
    """ class to display posts from selected category """
    model = models.Category
    template_name = 'posts/category_post.html'
    paginate_by = 7

    def get_queryset(self):
        """ self.kwargs.get method will get the username form the URL
        - see the url for this class """
        cat = models.Post.objects.filter(category=self.kwargs.get('category'))
        return cat


class PostDetailView(LoginRequiredMixin, generic.DetailView):
    """ class to display posts in detail """
    model = models.Post


class PostUpdateView(LoginRequiredMixin, generic.UpdateView):
    """ class to update the post """
    fields = ('title', 'text')
    model = models.Post

    def form_valid(self, form):
        """ function will set the author name automatically to the
        user logged in when post.author is passed inside the template """
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """ func will prevent current user to update other users post """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    """ class to delete the post """
    model = models.Post
    success_url = reverse_lazy('posts:post_list')

    def test_func(self):
        """ func will prevent current user to delete other users post """
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


# ------------------------COMMENT VIEWS-------------------------------#


# class CommentPostView(LoginRequiredMixin, generic.CreateView):
#     form_class = forms.CommentForm
#     template_name = 'posts/post_comment.html'
#
#     def form_valid(self, form):
#         form.instance.comment_text = self.request.user
#         return super().form_valid(form)


@login_required
def add_comment_to_post(request, pk):
    """ To attach comments to the post"""
    post = get_object_or_404(models.Post, pk=pk)

    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        form.instance.author = request.user

        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_post = post
            comment.save()
            return redirect('posts:post_details', pk=post.pk)

    else:
        form = forms.CommentForm()

    return render(request, 'posts/comment_form.html', context={'form': form})


class CommentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = models.Comment
    template_name = 'posts/comment_confirm_delete.html'

    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        super().delete(*args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('posts:post_details', kwargs={'pk': self.object.comment_post.id})

    # def test_func(self):
    #     """ func will prevent current user to delete other users post """
    #     post = self.get_object()
    #     if self.request.user == post.author:
    #         return True
    #     return False


# ------------------------REPLY COMMENT VIEWS-------------------------------#

@login_required
def reply_to_comment(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)

    if request.method == 'POST':
        reply_form = forms.ReplyCommentForm(request.POST)

        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.reply_comment = comment
            reply.save()
            return redirect('posts:post_details', pk=comment.pk)

    else:
        reply_form = forms.ReplyCommentForm()

    return render(request, 'posts/reply_comment_form.html', context={'reply_form': reply_form})
