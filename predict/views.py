from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PredictionSerializer
import pickle
import os


class MLAPIView(APIView):
    def post(self, request):
        pickle_file_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
        with open(pickle_file_path, 'rb') as f:
            model = pickle.load(f)
        
        # Deserialize and validate the input data
        serializer = PredictionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extract the validated data from the serializer
        input_data = serializer.validated_data

        input_features = [
            input_data['gender'],
            input_data['married'],
            input_data['dependents'],
            input_data['education'],
            input_data['self_employed'],
            input_data['applicant_income'],
            input_data['coapplicant_income'],
            input_data['loan_amount'],
            input_data['loan_amount_term'],
            input_data['credit_history'],
            input_data['property_area']
        ]

        predictions = model.predict([input_features])
        loan_status = int(predictions[0])

        return Response({'loan_status': loan_status})

    def get(self, request):
        return HttpResponse("Loan Prediction is running...")