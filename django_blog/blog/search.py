from django.db.models import Q
from .models import Post

def post_search(query):
    if query:
        return Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).filter(status='published').distinct()
    return Post.objects.none()