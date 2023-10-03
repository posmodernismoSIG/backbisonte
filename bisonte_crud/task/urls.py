from django.urls import path, include
from rest_framework import routers
from task import views

router = routers.SimpleRouter()

router.register(r"task", views.TaskView)  # , basename="task")
urlpatterns = [path("api/v1/", include(router.urls))]
# urlpatterns = router.urls
