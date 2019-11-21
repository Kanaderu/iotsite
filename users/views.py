from rest_framework.views import APIView, status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions, status
from .serializers import AccountSerializerWithToken, RefreshTokenSerializer
from rest_framework_simplejwt.serializers import TokenObtainSlidingSerializer
from rest_framework_simplejwt.tokens import SlidingToken


class CreateAccountView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self,request):
        user = request.data.get('username')
        if not user:
            #return Response({'response' : 'error', 'message' : 'No data found'})
            return Response({
                'username': 'This field is required.'
            }, status=status.HTTP_400_BAD_REQUEST)

        serializer = AccountSerializerWithToken(data=request.data)
        if serializer.is_valid():
            saved_user = serializer.save()
        else:
            #return Response({"response" : "error", "message" : serializer.errors})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #return Response({"response" : "success", "message" : "Account created succesfully"})
        return Response({"message": "Account Created Successfully"}, status=status.HTTP_201_CREATED)


class LogoutView(GenericAPIView):
    serializer_class = RefreshTokenSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, *args):
        sz = self.get_serializer(data=request.data)
        sz.is_valid(raise_exception=True)
        sz.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListSlidingTokenView(GenericAPIView):
    serializer_class = TokenObtainSlidingSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        #print(dir(request))
        #Token.for_user(request.user)
        #print(self.serializer_class.get_token(request.user))
        #print(SlidingToken.for_user(request.user))

        return Response({'token': str(SlidingToken.for_user(request.user))})