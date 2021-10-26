from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


# Create your views here.

#To list all proposed posts Post
class PostListView(ListView):
    model = Post
    template_name = 'posts/post_list.html'
    fields = ['title', 'body', 'author'] 
    

#To see informations about trip in detail
class PostDetailView(DetailView): 
    model = Post
    template_name = 'posts/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        context['number_of_likes'] = likes_connected.number_of_likes()
        
        return context

#To edit new posts
class PostCreateView(CreateView): 
    model = Post
    template_name = 'posts/post_new.html'
    fields = ['title', 'body'] 
    
    #to fill authenticated user as author
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#update posts informations
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'posts/post_edit.html'
    fields = ['title', 'body']   


  #Delete posts
class PostDeleteView(DeleteView): 
    model = Post
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('home')

#Like a view
def LikeView(request, pk):
    
    post_id = request.POST.get('post-id')
    post =  get_object_or_404(Post, pk=post_id)   
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[post_id]))
