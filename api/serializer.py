from rest_framework import serializers

import api.models


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.App
        fields = [
            'id',
            'name',
            'url',
            'ratings',
            'dev_name',
            'version',
            'last_modified',
            'last_update_info'
            'count_reviews'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Review
        fields = [
            'id',
            'app',
            'description',
            'created_at',
            'last_update_info',
            'commentator_name',
            'rating',
            'is_notified',
            'language'
        ]


class SubscriptionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.SubscriptionType
        fields = [
            'id',
            'name',
            'price',
            'description'
        ]


class Subscription(serializers.ModelSerializer):
    class Meta:
        model = api.models.Subscription
        fields = [
            'user_id',
            'subscription_type_id',
            'created_at',
            'expired_at'
        ]


class IntegrationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.IntegrationType
        fields = [
            'name'
        ]


class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Integration
        fields = [
            'user_id',
            'app_id',
            'integration_type_id'
        ]