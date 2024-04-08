from django.urls import path, include

from rest_framework import routers



from . import views

router = routers.DefaultRouter()
router.register("/consumer", views.ConsumerViewSet)
router.register("/calculate", views.CalculatorViewSet, basename="calculate")


urlpatterns = [
    path("api", include(router.urls)),
    path("", views.ConsumerViewSet.list_consumers, name="list_consumers"),
    path("create", views.ConsumerViewSet.create_consumer, name="create_consumer"),
    path("calculate", views.CalculatorViewSet.calculate_view, name="calculate_view")
    ]
