from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    gender = serializers.IntegerField()
    married = serializers.IntegerField()
    dependents = serializers.IntegerField()
    education = serializers.IntegerField()
    self_employed = serializers.IntegerField()
    applicant_income = serializers.IntegerField()
    coapplicant_income = serializers.IntegerField()
    loan_amount = serializers.IntegerField()
    loan_amount_term = serializers.IntegerField()
    credit_history = serializers.IntegerField()
    property_area = serializers.IntegerField()
    # loan_status = serializers.IntegerField()