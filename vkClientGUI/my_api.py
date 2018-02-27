import main
import config
import json

passw = config.vkPassw
login = config.vkLogin
appId = config.appId
myId = config.myId
api = main.api


def parseJson(json_string, field1, field2):
    try:
        parsed_string = json.loads(json_string)
        substring = str(parsed_string[field1]).replace('[', '')
        substring = substring.replace(']', '')
        substring = substring.replace("'", '"')
        json_dict = json.loads(substring)
        return str(json_dict[field2])
    except (json.JSONDecodeError, TypeError):
        print('Error occurred')


def getFriends():
    resp3 = api.friends.get(user_id=myId, order='name', count='1000', offset='0', fields='name', name_case='nom')
    usersJsonList = resp3['items']
    config.count = 0
    for item in usersJsonList:
        name = str(item['first_name']) + ' ' + str(item['last_name'])
        user_id = str(item['id'])
        config.count += 1
        config.friends_dict.update({name: user_id})


def get_users(user_id):
    return api.users.get(user_ids=user_id)