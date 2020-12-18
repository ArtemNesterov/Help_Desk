from rest_framework import serializers

from help_desk.models import ClaimModel


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimModel
        fields = ('__all__')


class ForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimModel
        fields = ('__all__')
        read_only_fields = ('claim_topic', 'author', 'declined_status_count',
                            'id', 'create_at', 'update_at', 'delete_at')


class ForAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimModel
        fields = ('__all__')
        read_only_fields = ('claim_topic', 'text', 'image', 'priority', 'author', 'declined_status_count',
                            'id', 'create_at', 'update_at', 'delete_at')
