from rest_framework import serializers


class AppIdRequestSerializer(serializers.Serializer):
    app_id = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
