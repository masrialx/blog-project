from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, CategoryViewSet, TagViewSet, CommentViewSet, UserRegistrationViewSet, UserProfileViewSet

router = DefaultRouter()
router.register('posts', BlogPostViewSet)
router.register('categories', CategoryViewSet)
router.register('tags', TagViewSet)
router.register('register', UserRegistrationViewSet)
router.register('profiles', UserProfileViewSet)
router.register('comments', CommentViewSet)

urlpatterns = router.urls
