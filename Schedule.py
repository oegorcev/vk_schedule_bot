import Parser
from Constants import *
import datetime
import emoji

def make_Schedule(day, data):

    j = 0
    output = ''
    week = cur_week()

    if week == 0:
        output += u'Сейчас идет верхняя неделя.\n'
    else:
        output += u'Сейчас идет нижняя неделя.\n'

    if day == TODAY:
        curDay = datetime.date.today().weekday()
    else:
        curDay = (datetime.date.today().weekday() + 1) % 8

    for dat in data[curDay]:
        if j == 0:
            output += emoji.emojize(':white_check_mark:', use_aliases=True) + ' ' + (u'Сегодня ' if (day == TODAY) else u'Завтра ') + data[curDay][dat][0] + '.\n'
        else:
            if data[curDay][dat][week] == IF_ONLY_ONE_WEEK:
                output += emoji.emojize(':o:', use_aliases=True) + dat.split(' ')[1] + ' ' + (emoji.emojize(':smirk:', use_aliases=True) + u'Пары нет' if data[curDay][dat][(week + 1) % 2] == '' else data[curDay][dat][(week + 1) % 2]) + '\n'
            else:
                output += emoji.emojize(':o:', use_aliases=True) + dat.split(' ')[1] + ' ' + (emoji.emojize(':smirk:', use_aliases=True) + u'Пары нет' + emoji.emojize(':smirk:', use_aliases=True) if data[curDay][dat][week] == ''  else data[curDay][dat][week]) + '\n'

        j += 1

    return output


def make_output_data(data, action):

    output = ''

    # Today && Tomorrow
    if action == TODAY or action == TOMORROW:
        output = make_Schedule(action, data)

    # Weekly
    if action == FULL_WEEK:
        for day in data:
            j = 0
            for dat in day:
                if j == 0:
                    output += emoji.emojize(':white_check_mark:', use_aliases=True) + ' ' + day[dat][0] + '\n'
                else:
                    if day[dat][0] == IF_ONLY_ONE_WEEK or day[dat][1] == IF_ONLY_ONE_WEEK:
                        output += emoji.emojize(':o:', use_aliases=True) + dat.split(' ')[1] + ' ' + ((emoji.emojize(':smirk:', use_aliases=True) + u'Пары нет' + emoji.emojize(':smirk:', use_aliases=True) if day[dat][1] == ''  else day[dat][1]) if day[dat][1] != IF_ONLY_ONE_WEEK else (emoji.emojize(':smirk:', use_aliases=True) + u'Пары нет' + emoji.emojize(':smirk:', use_aliases=True) if day[dat][0] == ''  else day[dat][0])) + '\n'
                    else:
                        output += emoji.emojize(':o:', use_aliases=True) + dat.split(' ')[1] + u' Верхняя неделя: ' + (emoji.emojize(':smirk:', use_aliases=True) + u'Пары нет' + emoji.emojize(':smirk:', use_aliases=True) if day[dat][1] == ''  else day[dat][1]) + '\n'
                        output += u' Нижняя неделя: ' + (emoji.emojize(':smirk:', use_aliases=True) + u'Пары нет' + emoji.emojize(':smirk:', use_aliases=True) if day[dat][0] == ''  else day[dat][0]) + '\n'

                j += 1
            output += '\n'

    if action == EXAMS:
        output += '\n'
        for day in data:
            j = 0
            for dat in day:
                if j == 0:
                    output += emoji.emojize(':white_check_mark:', use_aliases=True) + ' ' + day[dat] + '\n'
                else:
                    output += emoji.emojize(':o:', use_aliases=True) + dat.split(' ')[1] + ' ' + day[dat] + '\n'

                j += 1
            output += '\n'

    return output


def get_Schedule(request, action):

    # Ищем расписание для заочников или нет
    flag = (u'з' in request)

    request = ascii(request)
    request = request.replace('\\u', '%u')
    request = request.replace('\'', '')

    s = 'http://asu.tti.sfedu.ru/Raspisanie/ShowRaspisanie.aspx?Substance=' + request + '&isPotok=' + cur_pot() + '&Semestr=' + cur_sem()

    data = Parser.parse(Parser.get_html(s))
    dataEx = []
    '''
    if data:
        dataEx = Parser.parse_exams(Parser.get_html(s))
    else:
        return u'Такой группы не существует :('
    
    '''
    print(1)

    if data and dataEx and flag == 0:
        output = make_output_data(data, action)
        output += u'\nРасписание экзаменов:'
        output += make_output_data(dataEx, EXAMS)
    else:
        if data and flag == 0:
            output = make_output_data(data, action)
            output += u'\nЭкзамены ещё не завезли :)' + emoji.emojize(':beer:', use_aliases=True)
        else:
            if dataEx:
                output = make_output_data(dataEx, EXAMS)
    
    return output
