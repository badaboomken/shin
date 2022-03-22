import vk_api
import time

token = '026a85a639f1c565d1c27d964b577911ec2f459cb6ff24fff111abeca48721bf4281a9ccc333d2352e5a8'

vk = vk_api.VkApi(token=token)
vk._auth_token()

value = {
    'offset': 0,
    'count': 20,
    'filter': 'unanswered'
}

q = ['сколько месяцев в году?', 'столица россии', 'сколько бит в байте', '']
a = [[12, 3, 6, 11],
    ['росcия', 'москва', 'ярославль', 'питер'],
    [9, 24, 8, 1024]]
keys = [1, 2, 3]
i = 0 
score = 0
mes = ''
while True:
    messages = vk.method('messages.getConversations', value)
    print(messages)
    if messages['count'] >= 1:
        user_id = messages['items'][0]['last_message']['from_id']
        text = messages['items'][0]['last_message']['text'].lower()
        if i == 0 or text == str(keys[i - 1]):
            if i != 0:
                score += 10
                mes = 'Your score: ' +str(score)
                vk.method('messages.send', {'peer_id': user_id, 'message': mes, 'random_id': 0})
            if i == 3:
                vk.method('messages.send', {'peer_id': user_id, 'message': 'you win', 'random_id': 0})
                break
            mes = q[i] + '\n 1. ' + str(a[i][0])
            mes += '\n 2. ' + str(a[i][1])
            mes += '\n 3. ' + str(a[i][2])
            mes += '\n 4. ' + str(a[i][3])
            mes += '\n введите ответ цифрой'
            vk.method('messages.send', {'peer_id': user_id, 'message': mes, 'random_id': 0})
            i += 1

        '''vk.method('messages.send', {'peer_id': user_id, 'message': 'Hello, nice to meet you', 'random_id': 0})'''

    time.sleep(1)


