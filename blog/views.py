from datetime import timezone
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import BlogPost, Category, Tag, Comment, UserProfile
from .serializers import (
    BlogPostSerializer, CategorySerializer, TagSerializer,
    CommentSerializer, UserRegistrationSerializer, UserProfileSerializer
)
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.exceptions import ValidationError 


class BlogPostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post = serializer.save(author=self.request.user)
        if post.is_published and not post.published_date:
            post.published_date = timezone.now()
            post.save()

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        if request.user in post.likes.all():
            return Response({'status': 'post already liked'}, status=400)

        post.likes.add(request.user)
        return Response({'status': 'post liked'})

    def perform_update(self, serializer):
        post = self.get_object()
        if post.author == self.request.user or self.request.user.is_staff:
            serializer.save()
        else:
            raise permissions.PermissionDenied("You do not have permission to edit this post.")

    def perform_destroy(self, instance):
        if instance.author == self.request.user or self.request.user.is_staff:
            instance.delete()
        else:
            raise permissions.PermissionDenied("You do not have permission to delete this post.")


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]  

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAdminUser] 

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserRegistrationViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def perform_create(self, serializer):
        user = serializer.save()


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        if UserProfile.objects.filter(user=user).exists():
            raise ValidationError({"detail": "Profile already exists."})
        serializer.save(user=user)

    def perform_update(self, serializer):
      
        user_profile = self.get_object()
        if user_profile.user != self.request.user:
            raise permissions.PermissionDenied("You do not have permission to update this profile.")
        serializer.save()
