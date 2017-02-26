import users.serializers as s
from users.models import BasicUser

def jwt_response_payload_handler(token, user=None, request=None):
    #print(user.id)
    b_user = BasicUser.objects.get(pk=user.pk)
    print(b_user.user_type)
    return {
        'token': token,
        'user': s.UserSerializer(b_user, context={'request': request}).data
    }