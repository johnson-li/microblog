import unittest

import webrpc.api.user
import webrpc.impl.local.client


class TestUserLogic(unittest.TestCase):
    def __init__(self, method_name='runTest'):
        super(TestUserLogic, self).__init__(method_name)
        self.client = webrpc.impl.local.client.Client()

    def test_user(self):
        info = webrpc.api.user.create_user(self.client, 'johnson', '1@j.com', 'password')
        user = webrpc.api.user.get_user(self.client, info['user_id'])
