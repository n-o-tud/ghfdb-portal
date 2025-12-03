from django.urls import include, path

urlpatterns = [
    path("", include("fairdm.conf.urls")),
    path("", include("ghfdb.urls")),
    path("api/", include("restapi.urls")),
    # path("", include("review.urls")), # comment out to reduce influence
]
