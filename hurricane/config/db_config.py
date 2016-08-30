import db.impl.sqlite.client


def get_client():
    return db.impl.sqlite.client.Client()
