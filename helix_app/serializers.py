from rest_framework import serializers

class HelixParametersSerializer(serializers.Serializer):
    radius = serializers.FloatField(min_value=0.5, max_value=3.0, default=1.0)
    pitch = serializers.FloatField(min_value=1.0, max_value=5.0, default=3.4)
    num_turns = serializers.IntegerField(min_value=1, max_value=20, default=10)
    points_per_turn = serializers.IntegerField(min_value=50, max_value=200, default=100)
    num_base_pairs = serializers.IntegerField(min_value=5, max_value=50, default=20) 