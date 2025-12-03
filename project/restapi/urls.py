from django.urls import path
from . import measurements_viewsets, samples_viewsets


# # example using viewsets and routers
from rest_framework_nested import routers
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

router = DefaultRouter()
router.register(
    r"surface-heat-flow",
    measurements_viewsets.SurfaceHeatFlowViewSet,
    basename="/surface-heat-flow",
)
router.register(
    r"heat-flow", measurements_viewsets.HeatFlowViewSet, basename="/heat-flow"
)
router.register(
    r"thermal-gradient",
    measurements_viewsets.ThermalGradientViewSet,
    basename="/thermal-gradient",
)
router.register(
    r"interval-conductivity",
    measurements_viewsets.IntervalConductivityViewSet,
    basename="/interval-conductivity",
)
router.register(
    r"heat-flow-site",
    samples_viewsets.HeatFlowSiteViewSet,
    basename="/heat-flow-site",
)
router.register(
    r"heat-flow-interval",
    samples_viewsets.HeatFlowIntervalViewSet,
    basename="/heat-flow-interval",
)

urlpatterns = router.urls


urlpatterns += [
    path(
        "schema/",
        SpectacularAPIView.as_view(urlconf="restapi.urls"),
        name="schema",
    ),
    path(
        "docs/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "docs/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]
