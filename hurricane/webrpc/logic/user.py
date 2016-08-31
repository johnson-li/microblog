import config.db_config
import db.api.user
import utils.logic

db_client = config.db_config.get_client()


def get_user(user_id):
    db_filter = utils.logic.SingleExpression('user_id', user_id, utils.logic.Comparator.EQ)
    return db.api.user.get_user(db_client, db_filter)


def create_user(name, email, password, bio=''):
    data = {'email': email, 'name': name, 'password': password, 'bio': bio}
    return db.api.user.create_user(db_client, data)
