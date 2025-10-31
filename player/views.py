from django.shortcuts import render
from .models import Video
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class VideoListView(ListView):
    model = Video
    template_name = "videos/video_list.html"
    context_object_name = "videos"

