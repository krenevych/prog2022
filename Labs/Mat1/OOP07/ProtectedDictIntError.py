# class ProtectedDictIntError(KeyError):
#
#     TYPE_PERMISSION_MODIFICATION_ERROR = 1  # Зміна значення за ключем заборонена
#     TYPE_KEY_NOT_INTEGER_ERROR = 2  # Ключ словника може бути лише цілим числом
#
#     def __init__(self, message, error_type):
#         self.message = message
#         self.error_type = error_type
#
#     def __str__(self):
#         return self.message

class ProtectedDictIntError(KeyError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ProtectedDictIntChangeValueError(ProtectedDictIntError):
    def __init__(self, key, old_value, new_value):
        super().__init__("Зміна значення за ключем заборонена!")
        self.key = key
        self.old_value = old_value
        self.new_value = new_value

class ProtectedDictIntKeyNonIntegerError(ProtectedDictIntError):
    def __init__(self, key):
        super().__init__("Ключ словника може бути лише цілим числом")
        self.key = key
