class KeyPair:
    """Данный класс используется для подписи операций пользователя. Обеспечивает аутентичность приложения"""
    publicKey = ''
    __privateKey = ''

    def __init__(self, publicKey, privateKey):
        self.publicKey = publicKey
        self.__privateKey = privateKey

