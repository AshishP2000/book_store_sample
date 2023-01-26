import logging

import jwt

logging.basicConfig(filename='book_store.log', level=logging.INFO)


class JWT:
    def encode(self, data):
        try:
            encoded_jwt = jwt.encode(data, "secret", algorithm="HS256")
            return encoded_jwt
        except Exception as ex:
            logging.error(ex)

    def decode(self, token):
        try:
            return jwt.decode(token, "secret", algorithms=["HS256"])
        except jwt.exceptions.ExpiredSignatureError:
            raise Exception("token expired")
        except jwt.exceptions.InvalidSignatureError:
            raise Exception("invalid token")
        except Exception as ex:
            logging.error(ex)
