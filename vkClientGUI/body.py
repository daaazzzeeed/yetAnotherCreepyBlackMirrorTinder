from my_api import *


getFriends()
print('q чтобы выйти\ng получить последнее сообщение\nm отправить сообщение\nf список друзей' )

while 1:
    try:
        req = input()
        if req == 'q':
            break
        elif req == 'g':
            resp = api.messages.get(count='1')
            resp = str(resp).replace("'", '"')
            us_id = parseJson(resp, 'items', 'user_id')
            resp2 = get_users(us_id)
            resp2 = str(resp2).replace("'", '"')
            resp2 = resp2.replace('[','')
            resp2 = resp2.replace(']','')
            resp2 = json.loads(resp2)
            print('Сообщение : ' + parseJson(resp, 'items', 'body') + ' от : ' + resp2['first_name'] + ' ' + resp2['last_name'])
        elif req == 'm':
            print('введите текст : ')
            text_msg = input()
            print('введите имя пользователя')
            name_user = input()
            print('Сообщение ' + '[' + text_msg + '] будет отправлено ' + '[' + name_user + ']')
            print('Отправить? y/n')
            decision = input()
            if decision == 'y':
                userId = config.friends_dict.get(name_user)
                api.messages.send(user_id=userId, message=text_msg)
                print('Отправлено')
            elif decision == 'n':
                print('Сообщение не будет отправлено')
        elif req == 'f':
            for item in config.friends_dict:
                print(item)
            print('Количество друзей : ' + str(config.count))

    except KeyboardInterrupt:
        print('input interrupted')
        break