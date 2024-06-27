from django.shortcuts import render, redirect
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainSerializer, UserSerializer
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.urls import reverse
from .models import User  # Assuming User model is defined in your app

class CustomTokenObtainView(APIView):
    permission_classes = (AllowAny,)  # Allow any user to obtain a token

    def post(self, request, *args, **kwargs):
        serializer = CustomTokenObtainSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            refresh = RefreshToken.for_user(user)
            request.session['refresh_token'] = str(refresh)
            request.session['access_token'] = str(refresh.access_token)
            request.session['user'] = UserSerializer(user).data
            
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': UserSerializer(user).data,
                'message': 'Authentication successful'
            })
        else:
            return Response({"error": "Authentication failed"}, status=status.HTTP_401_UNAUTHORIZED)

class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        user = request.user 
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user = self.request.user
            context['email'] = user.email
            context['name'] = user.first_name
            context['role'] = user.role  # Assuming 'role' is a field in your User model
            
        categories = [
            {
                'name': 'User Management',
                'links': [
                    # Add your links here as needed
                ]
            },
            {
                'name': 'Partner Management',
                'links': [
                    # Add your links here as needed
                ]
            },
            {
                'name': 'Employee Management',
                'links': [
                    # Add your links here as needed
                ]
            },
        ]

        context['categories'] = categories
        return context

    def dispatch(self, request, *args, **kwargs):
        # Redirect to login page if user is not authenticated
        if not request.user.is_authenticated:
            return redirect(reverse('user_login'))  # Adjust 'user_login' to your login URL name
        return super().dispatch(request, *args, **kwargs)


def login_view(request):
    if request.method == 'POST':
        # Retrieve email and password from the POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Validate email and password
        if email and password:
            # Authenticate user
            user = authenticate(request, email=email, password=password)

            if user is not None:
                # Login user
                login(request, user)

                # Redirect to home page if authentication is successful
                return redirect('home')
            else:
                # Handle authentication failure
                return render(request, 'login.html', {'error': 'Invalid email or password'})
        else:
            # Handle empty form fields
            return render(request, 'login.html', {'error': 'Email and password are required.'})
    else:
        # Render the login form for GET requests
        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    # Optionally, you can clear session data
    request.session.flush()
    return redirect('user_login')  # Redirect to the login page


