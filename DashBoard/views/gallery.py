from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from ..models import Gallery
from ..forms import GalleryForm
from django.contrib import messages 


class AddGalleryView(View):
    def get(self, request):
        form = GalleryForm()
        return render(request, 'DashBoard/gallery/add.html', {'form': form})

    def post(self, request):
        data = request.POST.copy()
        data['user'] = request.user.id
        form = GalleryForm(data, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image added to Gallery Successfully')
            return redirect('DashBoard:listGallery')
        else:
            messages.error(request, form.errors)
        return redirect('DashBoard:addGallery')


class ListGalleryView(TemplateView):
    def get(self, request):
        if request.user.is_staff:
            images = Gallery.objects.all()
        else:
            images = Gallery.objects.filter(user=request.user.id)
        return render(request, 'DashBoard/gallery/list.html', {'images': images})


class DeleteGalleryView(View):
    def get(self, request, pk):
        Gallery.objects.filter(pk=pk).delete()
        messages.success(request, 'Image deleted from Gallery Successfully')
        return redirect('DashBoard:listGallery')


class EditGalleryView(View):
    def get(self, request, pk):
        image = Gallery.objects.get(pk=pk)
        form = GalleryForm(instance=image)
        return render(request, 'DashBoard/gallery/edit.html', {'form': form})

    def post(self, request, pk):
        image = Gallery.objects.get(pk=pk)
        data = request.POST.copy()
        data['user'] = request.user.id
        form = GalleryForm(data, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            messages.success(request, 'Image updated in Gallery Successfully')
            return redirect('DashBoard:listGallery')
        else:
            messages.error(request, form.errors)
        return redirect('DashBoard:editGallery', pk=pk)
    

class AllGalleryView(View):
    def get(self, request):
        images = Gallery.objects.all()
        return render(request, 'Home/gallery.html', {'images': images})
