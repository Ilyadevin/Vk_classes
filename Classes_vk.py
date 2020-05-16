import vk_api
import requests


class MutualFriends:
    def __init__(self, user_ids_vk):
        self.user_ids_vk = user_ids_vk

    def check_friend_status(self):
        connecting = requests.get()


def launching_class():
    users = list()
    user_one_by_one = input('Введите id профилей => ')
    users.append(user_one_by_one.split(" "))
    start = MutualFriends(users)
    start.user_ids_vk()


launching_class()
