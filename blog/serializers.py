from rest_framework import serializers
from .models import BlogPost, Category, Tag, Comment, UserProfile
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BlogPostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, required=False)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'created_date', 'is_published', 'likes', 'image']
        read_only_fields = ['author', 'created_date', 'likes']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = BlogPost(**validated_data)
        post.author = self.context['request'].user  # Set the author to the current user
        post.save()

        for tag in tags_data:
            tag_instance, created = Tag.objects.get_or_create(**tag)
            post.tags.add(tag_instance)

        return post

from rest_framework import serializers
from .models import Comment  # Assume Comment is your model

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'user']
        read_only_fields = ['user']  # Mark user as read-only

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user  # Automatically set the user
        return super().create(validated_data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.is_active = False  # New users are inactive by default
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
