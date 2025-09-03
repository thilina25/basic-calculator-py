from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer


# A ViewSet automatically provides CRUD operations (Create, Read, Update, Delete)
class TaskViewSet(viewsets.ModelViewSet):
    # Define the queryset of objects this ViewSet will manage
    queryset = Task.objects.all()
    
    # Define which serializer to use for converting Task objects <-> JSON
    serializer_class = TaskSerializer
