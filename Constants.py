import datetime
import emoji

IF_ONLY_ONE_WEEK = 'full'
If_TWO_WEEKS = 'true'
TODAY = '1'
TOMORROW = '2'
FULL_WEEK = '3'
EXAMS = '4'
HELP = u'Чтобы воспользоваться ботом напиши такую команду:\n[Группа] [Действие]\nСписок доступных действий:\n1 - расписание на сегодня;\n2 - расписание на завтра;\n3 - расписание на неделю.\nПример: КТбо3-8 1\n'
ERROR = emoji.emojize(':x:', use_aliases=True) + u'Сервер в данный момент недоступен' +  emoji.emojize(':x:', use_aliases=True)
BAD_GROUP = U'уэбо3-1'
REPAIR_BAD_GROUP = U'Уэбо3-1'

def cur_week():

    # Cur number of week isocalendar()[1]
    CUR_WEEK = (datetime.date.today().isocalendar()[1] - 2) % 2

    return CUR_WEEK


def cur_pot():

    # Magic (cur year isocalendar()[0]) 213 - half + 30 of year
    curday = datetime.date.today().day
    curpot = 121

	#curpot = 121

    return str(curpot)

def cur_sem():

    curday = datetime.date.today().day
    if 213 > curday:
        cursem = 2
    else:
        cursem = 1

	#cursem = 1

    return str(cursem)
