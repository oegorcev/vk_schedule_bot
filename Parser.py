# coding: utf8
import urllib.request
from bs4 import BeautifulSoup
from Constants import *


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', id='tblRaspis')

    projects = []
    i = 1

    if table.find_all('tr'):
        for row in table.find_all('tr')[2:]:
            cols = row.find_all('td')

            if i % 2:
                projects.append({
                    '8 day': (cols[0].text, 'day'),
                    '1 8:00-9:35  ': (cols[1].text, IF_ONLY_ONE_WEEK) if (cols[1]['class'] == ['row_rowspan']) else (cols[1].text, If_TWO_WEEKS),
                    '2 9:50-11:25 ': (cols[2].text, IF_ONLY_ONE_WEEK) if (cols[2]['class'] == ['row_rowspan']) else (cols[2].text, If_TWO_WEEKS),
                    '3 11:55-13:30': (cols[3].text, IF_ONLY_ONE_WEEK) if (cols[3]['class'] == ['row_rowspan']) else (cols[3].text, If_TWO_WEEKS),
                    '4 13:45-15:20': (cols[4].text, IF_ONLY_ONE_WEEK) if (cols[4]['class'] == ['row_rowspan']) else (cols[4].text, If_TWO_WEEKS),
                    '5 15:50-17:25': (cols[5].text, IF_ONLY_ONE_WEEK) if (cols[5]['class'] == ['row_rowspan']) else (cols[5].text, If_TWO_WEEKS),
                    '6 17:40-19:15': (cols[6].text, IF_ONLY_ONE_WEEK) if (cols[6]['class'] == ['row_rowspan']) else (cols[6].text, If_TWO_WEEKS),
                    '7 19:30-21:05': (cols[7].text, IF_ONLY_ONE_WEEK) if (cols[7]['class'] == ['row_rowspan']) else (cols[7].text, If_TWO_WEEKS)
               })
            else:
                if cols:
                    j = 0
                    for cnt in projects[len(projects) - 1]:
                        if projects[len(projects) - 1][cnt][1] == If_TWO_WEEKS:
                            projects[len(projects) - 1][cnt] = (projects[len(projects) - 1][cnt][0], cols[j].text)
                            j += 1

                else:
                    for cnt in projects[len(projects) - 1]:
                        if projects[len(projects) - 1][cnt][1] == If_TWO_WEEKS:
                            projects[len(projects) - 1][cnt][1] = (projects[len(projects) - 1][cnt][0], '')
            i += 1

    return projects


def parse_exams(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', id='tblRaspisZaoch')

    projects = []
    i = 1

    if table.find_all('tr'):
        for row in table.find_all('tr')[2:]:
            cols = row.find_all('td')

            if i % 2:
                projects.append({
                    '8 day': cols[0].text,
                    '1 8:00-9:35  ': cols[1].text,
                    '2 9:50-11:25 ': cols[2].text,
                    '3 11:55-13:30': cols[3].text,
                    '4 13:45-15:20': cols[4].text,
                    '5 15:50-17:25': cols[5].text,
                    '6 17:40-19:15': cols[6].text,
                    '7 19:30-21:05': cols[7].text,
               })

            i += 1

    return projects


# For local Debuging
'''def main():

    request = 'КТбо3-8'
    cursem = '2'
    curpot = '156'
    week = 0
    action = 1

    request = ascii(request)
    request = request.replace('\\u', '%u')
    request = request.replace('\'', '')

    s = 'http://sfedu-tgn.ru/Raspisanie/ShowRaspisanie.aspx?Substance=' + request + '&isPotok=' + curpot + '&Semestr=' + cursem


    data = parse(get_html(s))

    output = make_output_data(data, action, week)

    print(output)

if __name__ == '__main__':
    main()
'''





