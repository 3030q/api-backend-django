from rest_framework import serializers

from api.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
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
        model = App

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
