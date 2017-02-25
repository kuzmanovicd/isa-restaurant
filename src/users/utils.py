import users.serializers as s

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': s.UserSerializer(user, context={'request': request}).data
    }