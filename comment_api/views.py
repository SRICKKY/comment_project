from django.shortcuts import render
from .serializers import CommentSerializer
from .models import Comment
from rest_framework import viewsets, permissions

class CommentView(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
	# permission_classes = (permissions.IsAuthenticatedOrReadOnly,)