class NostrMQError(Exception):
    pass


class PublishError(NostrMQError):
    pass


class SignatureError(NostrMQError):
    pass
