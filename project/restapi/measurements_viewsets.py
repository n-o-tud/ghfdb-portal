from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import viewsets
from drf_spectacular.utils import OpenApiParameter, extend_schema

from heat_flow.models.measurements import (
    SurfaceHeatFlow,
    HeatFlow,
    ThermalGradient,
    IntervalConductivity,
)

from .measurements_serializers import (
    SurfaceHeatFlowSeriealizer,
    HeatFlowSerializer,
    ThermalGradientSerializer,
    IntervalConductivitySerializer,
)


class SurfaceHeatFlowViewSet(viewsets.ReadOnlyModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_

    Returns:
        _type_: _description_
    """

    queryset = SurfaceHeatFlow.objects.all()
    serializer_class = SurfaceHeatFlowSeriealizer

    @extend_schema(
        summary="Surface Heat Flow List",
        description="Retrieve a list of all Surface Heat Flow measurements.",
        responses=SurfaceHeatFlowSeriealizer(many=True),
    )
    def list(self, request):
        data = self.serializer_class(self.queryset, many=True).data
        if not data:
            return Response({"message": "No Surface Heat Flow data found."}, status=404)
        else:
            return Response(data)


class HeatFlowViewSet(viewsets.ReadOnlyModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_
    """

    queryset = HeatFlow.objects.all()
    serializer_class = HeatFlowSerializer

    @extend_schema(
        summary="Heat Flow List",
        description="Retrieve a list of all Heat Flow measurements.",
        responses=HeatFlowSerializer(many=True),
    )
    def list(self, request, *args, **kwargs):
        data = self.serializer_class(self.queryset, many=True).data
        if not data:
            return Response({"message": "No Heat Flow data found."}, status=404)
        else:
            return Response(data)


class ThermalGradientViewSet(viewsets.ReadOnlyModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_
    """

    queryset = ThermalGradient.objects.all()
    serializer_class = ThermalGradientSerializer

    @extend_schema(
        summary="Thermal Gradient List",
        description="Retrieve a list of all Thermal Gradient measurements.",
        responses=ThermalGradientSerializer(many=True),
    )
    def list(self, request, *args, **kwargs):
        data = self.serializer_class(self.queryset, many=True).data
        if not data:
            return Response({"message": "No Thermal Gradient data found."}, status=404)
        else:
            return Response(data)


@extend_schema(
    description="ViewSet for managing Interval Conductivity measurements.",
)
class IntervalConductivityViewSet(viewsets.ReadOnlyModelViewSet):
    """_summary_

    Args:
        viewsets (_type_): _description_
    """

    queryset = IntervalConductivity.objects.all()
    serializer_class = IntervalConductivitySerializer

    @extend_schema(
        summary="Interval Conductivity List",
        description="Retrieve a list of all Interval Conductivity measurements.",
        responses=IntervalConductivitySerializer(many=True),
    )
    def list(self, request, *args, **kwargs):
        data = self.serializer_class(self.queryset, many=True).data
        if not data:
            return Response(
                {"message": "No Interval Conductivity data found."}, status=404
            )
        else:
            return Response(data)
