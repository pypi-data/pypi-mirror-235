KEY2VALUE = {}


def get_value(key):
    Config.objects.get(key=key)
