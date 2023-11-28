from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from task import views

router = routers.SimpleRouter()

router.register(r"task", views.TaskView)  # , basename="task")
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("docs", include_docs_urls(title="Tasks API")),
]
# urlpatterns = router.urls
