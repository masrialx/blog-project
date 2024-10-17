from rest_framework import serializers
from .models import BlogPost, Category, Tag, Comment, UserProfile
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BlogPostSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True, required=False)

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'author', 'category', 'tags', 'created_date', 'is_published', 'likes', 'image']
        read_only_fields = ['author', 'created_date', 'likes']

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = BlogPost(**validated_data)
        post.author = self.context['request'].user
        post.save()
        post.tags.set(tags_data)
        return post

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)
        instance.tags.set(tags_data)
        return instance


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'user']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
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
        user.set_password(validated_data['password'])
        user.is_active = False  # New users are inactive by default
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
