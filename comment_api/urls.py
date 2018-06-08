from django.conf.	urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.documentation import include_docs_urls
from .views import CommentView

router = DefaultRouter()
router.register('comment',CommentView)

urlpatterns = [
	url('^', include(router.urls)),
	url(r'^docs/', include_docs_urls(title="Comment API"))
]