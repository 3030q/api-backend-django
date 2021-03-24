from rest_framework import serializers

from api.models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = ['id',
                  'name',
                  'url',
                  'ratings',
                  'dev_name',
                  'version',
                  'last_modified',
                  'last_update_info'
                  'count_reviews'
                  ]
