from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']      # 어떤 필드들을 입력받을 것인지 설정
    success_url = reverse_lazy('list') # 작성 완료하고 이동할 페이지
    template_name_suffix = '_create'   # 사용할 템플릿의 접미사만 변경하는 설정값. bookmark_create 템플릿 사용

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'   # 사용할 템플릿의 접미사만 변경하는 설정값. bookmark_update 템플릿 사용

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list') # 삭제 완료하고 이동할 페이지
