import vk
import requests
import time


class MutualFriends:
    def __init__(self, user_ids_vk):
        self.user_ids_vk = user_ids_vk
        self.cache_friends = dict()
        self.names = dict()

    def get_friends(self):
        if self in self.cache_friends:
            return self.cache_friends[self]
        else:
            time.sleep(1)
            while 1:
                try:
                    fr = vk.friends.get(user_id=self)
                except Exception as e:
                    if str(e).find('Access denied: user deactivated.') > -1:
                        return list()
                    else:
                        print(e)
                        time.sleep(5)
                else:
                    fr = set(fr['items'])
                    self.cache_friends[self] = fr
                    return fr

    def get_cfriends(self, uid2):
        time.sleep(1)
        while 1:
            try:
                fr = vk.friends.getMutual(source_uid=self, target_uid=uid2)
            except Exception as e:
                print(e)
                time.sleep(5)
            else:
                return set(fr)

    def get_name(self):
        if self in self.names:
            return self.names[self]
        else:
            time.sleep(1)
            while 1:
                try:
                    u = vk.users.get(user_ids=self)
                except Exception as e:
                    print(e)
                    time.sleep(5)
                else:
                    name = u[0]['first_name'] + ' ' + u[0]['last_name'] + ' (' + str(self) + ')'
                    self.names[self] = name
                    return name

    def check_friend_status(self):
        while 1:
            ids = rex.sub(' ', ids)
            ids = [int(i) for i in ids.split(' ') if len(i) > 0]
            friends = []
            cfriends = []

            print()
            for uid in ids:
                friends.append(MutualFriends.get_friends(self))
                print(MutualFriends.get_name(self))
            print()

            for i in range(len(ids)):
                cfriends.append([0] * len(ids))
                for j in range(i + 1, len(ids)):
                    # общие друзья
                    cfriends[i][j] = get_cfriends(ids[i], ids[j])
                    if ids[i] in friends[j]:
                        print(get_name(ids[i]), 'дружит с', get_name(ids[j]))
            print()


def launching_class():
    users = list()
    user_one_by_one = input('Введите через пробел ссылки на профили или id пользователей:\n')
    users.append(user_one_by_one.split(" "))
    start = MutualFriends(users)
    start.user_ids_vk()


launching_class()
