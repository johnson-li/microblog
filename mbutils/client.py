#!/usr/bin/env python
import json
import urllib

import requests

class Client(object):
    def __init__(self, api_url, dry_run=False):
        self.api_url = api_url
        self.dry_run = dry_run
        self.session = requests.Session()

    def _get(self, path, **kwargs):
        if self.dry_run:
            print 'GET {}{}{}'.format(
                self.api_url,
                path,
                '?'+urllib.urlencode(kwargs) if kwargs else '')
            return
        resp = self.session.get(self.api_url + path, params=kwargs)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'err_code': resp.status_code, 'err_msg': resp.content}

    def _post(self, path, **kwargs):
        if self.dry_run:
            print 'POST {}{} {}'.format(
                self.api_url,
                path,
                json.dumps(kwargs))
            return
        resp = self.session.post(self.api_url + path, json=kwargs)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {'err_code': resp.status_code, 'err_msg': resp.content}

    def get_user(self, user_id):
        return self._get('/users/{}'.format(user_id))

    def create_user(self, username, email, password, **kwargs):
        return self._post('/users/',
                          username = username,
                          email = email,
                          password = password,
                          **kwargs)

    def follow(self, user_id, other_id):
        return self._post('/users/{}/follow/{}'.format(user_id, other_id))

    def unfollow(self, user_id, other_id):
        return self._post('/users/{}/unfollow/{}'.format(user_id, other_id))

    def get_followers(self, user_id):
        return self._get('/users/{}/followers'.format(user_id))

    def get_followings(self, user_id):
        return self._get('/users/{}/followings'.format(user_id))

    def post_feed(self, user_id, content, **kwargs):
        return self._post('/feeds/',
                          user_id = user_id,
                          content = content,
                          **kwargs)

    def get_feed(self, feed_id):
        return self._get('/feeds/{}'.format(feed_id))

    def get_user_feeds(self, user_id):
        return self._get('/users/{}/feeds'.format(user_id))

    def get_friend_feeds(self, user_id):
        return self._get('/users/{}/friend-feeds'.format(user_id))

    def clear_all(self):
        return self._post('/clear-all')

if __name__ == '__main__':
    import random
    from pprint import pprint
    random_id = random.randint(1,100000)
    c = Client('http://localhost:7431')
    user = c.create_user('johnson+{}'.format(random_id), 'johnson+{}@gmail.com'.format(random_id), 'secret')
    pprint(user)
