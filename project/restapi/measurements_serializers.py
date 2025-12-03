from rest_framework import serializers
from heat_flow.models.measurements import (
    SurfaceHeatFlow,
    HeatFlow,
    ThermalGradient,
    IntervalConductivity,
)

from drf_spectacular.utils import extend_schema_serializer


# Define a serializer for the HeatFlowChild model. This serializer converts model instances to JSON and vice versa.
@extend_schema_serializer()
class SurfaceHeatFlowSeriealizer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    # value = serializers.DecimalField(
    #     max_digits=10,
    #     decimal_places=4,
    #     help_text="Measured surface heat flow value (mW/m²).",
    #     label="Surface Heat Flow Value",
    # )

    # uncertainty = serializers.DecimalField(
    #     max_digits=10,
    #     decimal_places=4,
    #     help_text="Uncertainty of the surface heat flow measurement (mW/m²).",
    #     label="Surface Heat Flow Uncertainty",
    # )

    # p_comment = serializers.CharField(
    #     max_length=255,
    #     help_text="Additional comments regarding the surface heat flow measurement.",
    #     label="Comments",
    #     allow_blank=True,
    # )

    # corr_HP_flag = serializers.BooleanField(
    #     help_text="Flag indicating if the heat production correction was applied.",
    #     label="Heat Production Correction Applied",
    # )

    # is_ghfdb = serializers.BooleanField(
    #     help_text="Indicates whether the data is part of the GHFDB database.",
    #     label="Is GHFDB Data",
    # )

    class Meta:
        # tie serializer to model
        model = SurfaceHeatFlow
        # specify fields to include in the serialized representation
        fields = "__all__"


@extend_schema_serializer()
class HeatFlowSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        model = HeatFlow
        fields = "__all__"


@extend_schema_serializer()
class ThermalGradientSerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        model = ThermalGradient
        fields = "__all__"


@extend_schema_serializer()
class IntervalConductivitySerializer(serializers.ModelSerializer):
    """_summary_

    Args:
        serializers (_type_): _description_
    """

    class Meta:
        model = IntervalConductivity
        fields = "__all__"
