from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import HelixParametersSerializer
import numpy as np

# Create your views here.

class HelixView(APIView):
    def post(self, request):
        serializer = HelixParametersSerializer(data=request.data)
        if serializer.is_valid():
            params = serializer.validated_data
            
            # Generate helix points
            t = np.linspace(0, 2*np.pi*params['num_turns'], params['points_per_turn']*params['num_turns'])
            
            # First strand
            x1 = params['radius'] * np.cos(t)
            y1 = params['radius'] * np.sin(t)
            z1 = (params['pitch'] * t) / (2*np.pi)
            
            # Second strand
            x2 = params['radius'] * np.cos(t + np.pi)
            y2 = params['radius'] * np.sin(t + np.pi)
            z2 = (params['pitch'] * t) / (2*np.pi)
            
            # Generate base pairs
            indices = np.linspace(0, len(x1)-1, params['num_base_pairs'], dtype=int)
            base_pairs = []
            
            for idx in indices:
                base_pairs.append({
                    'x': [float(x1[int(idx)]), float(x2[int(idx)])],
                    'y': [float(y1[int(idx)]), float(y2[int(idx)])],
                    'z': [float(z1[int(idx)]), float(z2[int(idx)])]
                })
            
            response_data = {
                'strand1': {
                    'x': x1.tolist(),
                    'y': y1.tolist(),
                    'z': z1.tolist()
                },
                'strand2': {
                    'x': x2.tolist(),
                    'y': y2.tolist(),
                    'z': z2.tolist()
                },
                'base_pairs': base_pairs
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
