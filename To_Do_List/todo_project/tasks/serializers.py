from rest_framework import serializers
from .models import Task   # Import the Task model

# Serializer for the Task model
# This will convert Task model instances into JSON (for API responses)
# and also validate/convert incoming JSON into Task model instances.
class TaskSerializer(serializers.ModelSerializer):
    
    # Meta class defines metadata for the serializer
    class Meta:
        model = Task              # The model that this serializer is based on
        fields = '__all__'        # Include all fields from the Task model
