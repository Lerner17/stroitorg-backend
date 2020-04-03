from rest_framework import serializers
from news.models import News


class AdminNewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'content',
                  'created_at', 'updated_at', 'is_active', 'slug', 'image')
