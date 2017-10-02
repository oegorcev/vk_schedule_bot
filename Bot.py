import time
import vk_api
import Schedule
import Constants
import Utilities

vk = vk_api.VkApi(token='217e08f0d936f161381e5cded8bd82798899c3388c3fdce95b9119494a380440a871e86c4f805498c97b5') #Авторизоваться как сообщество
vk.auth()
listqueue = []

values = {'out': 0, 'count': 1, 'time_offset': 1}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id': user_id, 'message': s})

while True:
    response = vk.method('messages.get', values)

    for item in response['items']:
            mas = item[u'body'].split(' ')
            print(item[u'user_id'], item[u'body'], item[u'date'])
            #if not item[u'id'] in listqueue:
            if len(mas) != 2:
                write_msg(item[u'user_id'], Constants.HELP)
            else:
                if mas[1] < u'0' or mas[1] > u'3':
                    write_msg(item[u'user_id'], Constants.HELP)
                else:
                    mas[0] = Utilities.change_register_group(mas[0])
                    try:
                        s = Schedule.get_Schedule(mas[0], mas[1])
                    except BaseException:
                        write_msg(item[u'user_id'], Constants.ERROR)
                    else:
                        write_msg(item[u'user_id'], s)
            vk.method('messages.delete', {'message_ids': item[u'id']})
            #listqueue.append(item[u'id'])

    #time.sleep(0.7)
