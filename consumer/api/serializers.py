from rest_framework import serializers

from consumer.models import CONSUMER_TYPE_CHOICES, Consumer

class ConsumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumer
        fields = "__all__"

class CalculatorSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()
    number3 = serializers.IntegerField()
    distributor_tax = serializers.FloatField()
    tax_type = serializers.ChoiceField(choices=CONSUMER_TYPE_CHOICES)