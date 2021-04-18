from rest_framework import serializers


class IntegrationIdRequestSerializer(serializers.Serializer):
    integration_id = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
