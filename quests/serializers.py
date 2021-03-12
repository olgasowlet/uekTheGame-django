from rest_framework import serializers

from quests.constants import TYPES
from quests.models import Quest


class QuestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quest
        fields = [
            'unique_number',
            'category',
            'type',
            'name',
            'credits',
            'terms',
        ]

    def validate(self, data):
        if data['type'][0] in data['category']:
            return data
        else:
            raise serializers.ValidationError("This type doesn't belong to chosen category")
