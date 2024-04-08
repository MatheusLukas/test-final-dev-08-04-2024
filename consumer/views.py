import json
from django.shortcuts import render
from requests import Response, post

from rest_framework import viewsets

from calculator import calculator
from consumer.api.serializers import CalculatorSerializer, ConsumerSerializer

from consumer.forms import CalculatorForm, ConsumerForm
from consumer.models import Consumer

# Create your views here.
class ConsumerViewSet(viewsets.ModelViewSet):
    queryset = Consumer.objects.all()
    serializer_class = ConsumerSerializer

    def list_consumers(request):
        consumers = Consumer.objects.all()
        serializer = ConsumerSerializer(consumers, many=True)
        return render(request, "consumer/list.html", {"consumers": serializer.data})
    
    def create_consumer(request):
        form = ConsumerForm()
        if request.method == "POST":
            form = ConsumerForm(request.POST)
            if form.is_valid():
                  consumer = form.save(commit=False)
                  result = calculator([consumer.consumption_range], consumer.distributor_tax, consumer.consumer_type)
                  consumer.discount_value = result[1]
                  consumer.save()
                  serializer = ConsumerSerializer(consumer)
                  post('http://localhost:8000/api/consumers/', data=serializer.data)

        return render(request, "consumer/create.html", {"form": form})
 
               

class CalculatorViewSet(viewsets.ViewSet):  
    def calculate_view(request):
        print("**************")
        form = CalculatorForm(request.POST)
        if form.is_valid():        
            data = form.data        
            print(data)
            serializer = CalculatorSerializer(data)          
            response = post('http://localhost:8000/api/calculate/', json=serializer.data)   
            print("-------------------------") 
            print(response)
            # result = json.loads(response.text)['result']
            # print(result)
        return render(request, 'consumer/calculator.html', {'form': form})    
    
            
        
    
        
    
        
    




