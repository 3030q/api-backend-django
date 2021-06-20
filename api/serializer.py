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
            'last_update_info',
            'count_reviews',
            'platform',
        ]


class AddAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.App
        fields = [
            'url',
            'platform',
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


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Subscription
        fields = [
            'id',
            'user',
            'subscription_type',
            'created_at',
            'expired_at'
        ]


class IntegrationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.IntegrationType
        fields = [
            'id',
            'name',
        ]


class IntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.Integration
        fields = [
            'id',
            'user',
            'app',
            'slack_token'
        ]
