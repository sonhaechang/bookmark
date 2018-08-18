from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from bookmark.models import Bookmark
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from bookmark.forms import BookmarkForm

# Create your views here.
def bookmark_list(request):
    bookmark = Bookmark.objects.all()
    return render(request, 'bookmark/bookmark_list.html', {'bookmark_list': bookmark})


# class BookmarkListView(ListView):
#     model = Bookmark
#
# bookmark_list = BookmarkListView.as_view()


def bookmark_create(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmark:list')
    else:
        form = BookmarkForm()
    return render(request, 'bookmark/bookmark_create.html', {'form': form})


# class BookmarkCreateView(CreateView):
#     model = Bookmark
#     template_name_suffix = '_create'
#     fields = ['site_name', 'url']
#     success_url = reverse_lazy('list')
#
#
# bookmark_create = BookmarkCreateView.as_view()


def bookmark_update(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect('bookmark:detail', bookmark.pk)

    else:
        form = BookmarkForm(instance=bookmark)

    return render(request, 'bookmark/bookmark_update.html', {
        'bookmark': bookmark,
        'form': form,
    })


# class BookmarkUpdateView(UpdateView):
#     model = Bookmark
#     fields = ['site_name', 'url']
#     template_name_suffix = '_update'
#     success_url = reverse_lazy('list')
#
#
# bookmark_update = BookmarkUpdateView.as_view()


def bookmark_delete(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        bookmark.delete()
        return redirect('bookmark:list')
    return render(request, 'bookmark/bookmark_confirm_delete.html', {'bookmark': bookmark})


# class BookmarkDeleteView(DeleteView):
#     model = Bookmark
#     success_url = reverse_lazy('bookmark:list')
#
#
# bookmark_delete = BookmarkDeleteView.as_view()


def bookmark_detail(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    return render(request, 'bookmark/bookmark_detail.html', {'bookmark': bookmark})


# class BookmarkDetailView(DetailView):
#     model = Bookmark
#
#
# bookmark_detail = BookmarkDetailView.as_view()
