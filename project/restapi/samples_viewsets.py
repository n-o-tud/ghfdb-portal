from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import OpenApiParameter, extend_schema

from heat_flow.models.samples import (
    HeatFlowSite,
    HeatFlowInterval,
)

from .samples_serializers import (
    HeatFlowSiteSerializer,
    HeatFlowIntervalSerializer,
)


class HeatFlowSiteViewSet(viewsets.ReadOnlyModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_

    Returns:
        _type_: _description_
    """

    queryset = HeatFlowSite.objects.all()
    serializer_class = HeatFlowSiteSerializer

    @extend_schema(
        summary="Heat Flow Site List",
        description="Retrieve a list of all Heat Flow Sites Samples.",
        responses=HeatFlowSiteSerializer(many=True),
    )
    def list(self, request):
        data = self.serializer_class(self.queryset, many=True).data
        if not data:
            return Response({"message": "No Heat Flow Site data found."}, status=404)
        else:
            return Response(data)


class HeatFlowIntervalViewSet(viewsets.ReadOnlyModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_

    Returns:
        _type_: _description_
    """

    queryset = HeatFlowInterval.objects.all()
    serializer_class = HeatFlowIntervalSerializer

    @extend_schema(
        summary="Heat Flow Interval List",
        description="Retrieve a list of all Heat Flow Interval Samples.",
        responses=HeatFlowIntervalSerializer(many=True),
    )
    def list(self, request):
        data = self.serializer_class(self.queryset, many=True).data
        if not data:
            return Response(
                {"message": "No Heat Flow Interval data found."}, status=404
            )
        else:
            return Response(data)
