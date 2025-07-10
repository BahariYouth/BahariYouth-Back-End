from rest_framework.response import Response
from rest_framework import status
from.serializers import UserSignupSerializer,UserLoginSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema



    
@swagger_auto_schema(
    methods=['POST'],
    request_body=UserSignupSerializer,
    operation_summary='User Registration',
    operation_description='Register new user',
    tags=['users']
)

@api_view(['POST'])
def signup(request):
    serializer = UserSignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                'token': token.key,
                'user':serializer.data
            
            }, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





    
@swagger_auto_schema(
    methods=['POST'],
    operation_summary='User Login',
    request_body=UserLoginSerializer,
    operation_description='Login user',
    tags=['users']
)

@api_view(['POST'])
def login(request):
    serializer = UserLoginSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    email = serializer.validated_data['email']
    password = serializer.validated_data['password']


    if not email or not password:
        return Response(
            {
                'en': 'Email and password are required.',
                'ar': 'البريد الإلكتروني وكلمة المرور مطلوبان.'
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    user = authenticate(request, email=email, password=password)

    if user is None:
        return Response(
            {
                'en': 'Invalid email or password.',
                'ar': 'البريد الإلكتروني أو كلمة المرور غير صحيحة.'
            },
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not user.is_active:
        return Response(
            {
                'en': 'This account has been disabled.',
                'ar': 'تم تعطيل هذا الحساب.'
            },
            status=status.HTTP_403_FORBIDDEN
        )

    token, _ = Token.objects.get_or_create(user=user)

    return Response(
        {
            'token': token.key,
            'user': {
                'id': user.id,
                'email': user.email,
                'full_name': user.full_name,
                'role': user.role,
            },
            'message': {
                'en': 'Login successful.',
                'ar': 'تم تسجيل الدخول بنجاح.'
            }
        },
        status=status.HTTP_200_OK
    )


