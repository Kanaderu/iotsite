from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework import permissions
from users.serializers import AccountSerializerWithToken


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