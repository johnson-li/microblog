import config.webrpc_config
import utils.exceptions
import webrpc.api.user

webrpc_client = config.webrpc_config.get_client()


def ping():
    return 'pang'


def login(user_id, password):
    user = webrpc.api.user.get_user(webrpc_client, user_id=user_id)[0]
    print user
    if not user:
        raise utils.exceptions.UserNotFoundException()
    if user['password'] != password:
        raise utils.exceptions.InvalidPasswordException()
    return user
