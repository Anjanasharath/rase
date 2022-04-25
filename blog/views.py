from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View, TemplateView
from django.urls import reverse_lazy
from blog.forms import BlogForm, BlogImageForm
from django.forms import inlineformset_factory

from blog.models import Blog, BlogComment, BlogImage


BlogFormset = inlineformset_factory(Blog, BlogImage, fields=('image',))

# Blog
class BlogListView(ListView):
    model = Blog
    template_name = "blog/list.html"


class BlogCreateView(View):
    template_name = "blog/create.html"
    blog_form = BlogForm
    blog_image_form = BlogImageForm

    def get(self, request):
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request):
        blog_form = self.blog_form(request.POST)
        blog_image_form = self.blog_image_form(request.POST, request.FILES)

        if (blog_form.is_valid() and blog_image_form.is_valid()):
            self.form_valid(blog_form)
        else:
            return self.form_invalid(blog_form,  blog_image_form)

        return redirect(reverse_lazy("Blog:blog_list"))

    def get_context_data(self, **kwargs):
        context = {
            "blog_form": self.blog_form(),
            "blog_image_form": self.blog_image_form()
        }

        return context

    def form_valid(self, blog_form):
        user = self.request.user
        blog = blog_form.save(commit=False)
        blog.user = user
        blog.save()

        images = self.request.FILES.getlist("image")

        for image in images:
            BlogImage.objects.create(image=image, blog=blog)

        return blog

    def form_invalid(self, blog_form, blog_image_form):
        context = {}
        context["blog_form"] = blog_form
        context["blog_image_form"] = blog_image_form

        return render(self.request, self.template_name, context)


class BlogDetailView(DetailView):
    model = Blog
    template_name = "blog/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = BlogImage.objects.filter(blog=self.object)
        context['blog_images'] = images
        return context


class BlogUpdateView(View):
    template_name = "blog/update.html"
    blog_form = BlogForm
    blog_image_form = BlogImageForm
    model = Blog

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get(self, request, pk):
        self.object = self.model.objects.get(id=pk)
        context = self.get_context_data()
        return render(request, self.template_name, context)

    def post(self, request, pk):
        self.object = self.model.objects.get(id=pk)
        blog_form = self.blog_form(request.POST, instance=self.object)
        blog_image_form = self.blog_image_form(request.POST, request.FILES)

        if (blog_form.is_valid() and blog_image_form.is_valid()):
            return self.form_valid(blog_form)
        else:
            return self.form_invalid(blog_form,  blog_image_form)

    def get_context_data(self, **kwargs):
        images = BlogImage.objects.filter(blog=self.object)
        context = {
            "blog_form": self.blog_form(instance=self.object),
            "blog_image_form": self.blog_image_form(),
            "blog_images": images,
            "blog": self.object
        }

        return context

    def form_valid(self, blog_form):
        blog = blog_form.save()
        images = self.request.FILES.getlist("image")

        for image in images:
            BlogImage.objects.create(image=image, blog=blog)

        return redirect(self.get_success_url())

    def form_invalid(self, blog_form, blog_image_form):
        context = self.get_context_data()
        return render(self.request, self.template_name, context)

    def get_success_url(self) -> str:
        return reverse_lazy('blog_detail', kwargs={'pk': self.kwargs['pk']})


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = "blog/delete.html"
    success_url = reverse_lazy("Blog:blog_list")


# Blog Comment
class BlogCommentListView(ListView):
    model = BlogComment
    template_name = "blog/comment/list.html"

    def get_queryset(self):
        blog = Blog.objects.get(id=self.kwargs['pk'])
        queryset = BlogComment.objects.filter(blog=blog)
        return queryset


class BlogCommentCreateView(CreateView):
    model = BlogComment
    template_name = "blog/comment/create.html"
    success_url = reverse_lazy("Blog:blog_comment_list")


class BlogCommentDetailView(DetailView):
    model = BlogComment
    template_name = "blog/comment/detail.html"


class BlogCommentUpdateView(UpdateView):
    model = BlogComment
    template_name = "blog/comment/update.html"

    def get_success_url(self) -> str:
        return reverse_lazy('Blog:blog_comment_detail', kwargs={'pk': self.kwargs['pk']})


class BlogCommentDeleteView(DeleteView):
    model = BlogComment
    template_name = "blog/comment/delete.html"
    success_url = reverse_lazy("Blog:blog_comment_list")


# Blog Image
class BlogImageDeleteView(View):
    template_name = "blog/delete.html"

    def get(self, request, pk, blog_image_id):
        return render(request, self.template_name)

    def post(self, request, pk, blog_image_id):
        self.object = self.get_object(blog_image_id)
        self.object.delete()
        return redirect(reverse_lazy('Blog:blog_update', kwargs={'pk': pk}))

    def get_object(self, blog_image_id):
        object = BlogImage.objects.get(id=blog_image_id)
        return object
