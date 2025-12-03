from rest_framework import serializers
from heat_flow.models.samples import HeatFlowSite, HeatFlowInterval
from fairdm_api.serializers import SampleSerializer

from drf_spectacular.utils import extend_schema_serializer


@extend_schema_serializer()
class HeatFlowSiteSerializer(SampleSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        model = HeatFlowSite
        fields = "__all__"


@extend_schema_serializer()
class HeatFlowIntervalSerializer(SampleSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        model = HeatFlowInterval
        fields = "__all__"
