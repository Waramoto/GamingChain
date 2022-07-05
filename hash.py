import hashlib


class Hash:
    @staticmethod
    def toSHA1(message: str):
        return hashlib.sha1(message.encode('utf-8')).hexdigest()
