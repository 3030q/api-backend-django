from rest_framework import serializers

import api.models


class TakeReviewRequestSerializer(serializers.Serializer):
    integration_id = serializers.IntegerField(required=True)
    platform = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class GooglePlayReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.GooglePlayReviews
        fields = [
            'id',
            'username',
            'text',
            'posted_at',
            'avatar_link',
            'rating',
            'relevance',
            'app_id'
        ]


class AppStoreReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.GooglePlayReviews
        fields = [
            'id',
            'app_id',
            'username',
            'text',
            'app_version',
            'rating',
            'relevance'
        ]


class AppGalleryReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = api.models.GooglePlayReviews
        fields = [
            'id',
            'app_id',
            'text',
            'posted_at',
            'avatar_link',
            'username',
            'rating',
            'relevance',
            'app_version'
        ]
