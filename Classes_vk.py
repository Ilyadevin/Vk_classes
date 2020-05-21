import vk_api
import requests
import time


class MutualFriends:
    def __init__(self, login, password, user_ids_vk):
        self.user_ids_vk = user_ids_vk
        self.login = login
        self.password = password
        self.request = None

    def finding_mutual_friend(self):
        try:
            time.sleep(1)
            self.request = vk_api.VkApi(self.login, self.password)
        except Exception as error:
            print(error)
        try:
            self.request.auth()
        except Exception as error:
            print(error)


def launching_class():
    users = list()
    user = input('Логин и пароль для пользователя > ')
    data_list = list(user.split(" "))
    user_one_by_one = input('Введите через запятую ссылки на профили или id пользователей (Не более ста) > ')
    users.append(user_one_by_one.split(" "))
    for id_vk in users:
        if id_vk == int():
            time.sleep(1)
            start = MutualFriends(data_list[0], data_list[1], id_vk)
            time.sleep(1)
            start.user_ids_vk()
        else:
            time.sleep(1.5)
            print('Please, write data in correct order')


launching_class()
