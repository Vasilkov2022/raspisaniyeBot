import requests
import json
from tinydb import TinyDB, Query
db = TinyDB('db.json')


# https://ruz.hse.ru/api/schedule/group/129742?start=2022.10.31&finish=2022.11.06&lng=2
def get_schedule_by_group(group='129742', start='2022.10.31', finish='2022.11.06' ):
    schedule_api = "https://ruz.hse.ru/api/schedule/group/{}?start={}&finish={}&lng=2"
    response = requests.get(schedule_api.format(group, start, finish))
    content = json.loads(response.content)
    for lesson in content:
        lesson_module = {
            'auditorium': lesson.get('auditorium'),
            'beginLesson': lesson.get('beginLesson'),
            'building': lesson.get('building'),
            'date': lesson.get('date'),
            'dayOfWeekString': lesson.get('dayOfWeekString'),
            'discipline': lesson.get('discipline'),
            'endLesson': lesson.get('endLesson'),
            'group': lesson.get('group'),
            'kindOfWork': lesson.get('kindOfWork'),
            'lecturer_rank': lesson.get('lecturer_rank'),
            'lecturer_title': lesson.get('lecturer_title'),
        }
        db.insert(lesson_module)


#https://ruz.hse.ru/api/search?term=БПАД22&type=group
def get_group_by_name(group_name='БПАД222'):
    group_api = 'https://ruz.hse.ru/api/search?term={}&type=group'
    response = requests.get(group_api.format(group_name))
    content = response.json()
    if not content:
        return None
    return content[0].get('id')


if __name__ == '__main__':
    print(get_group_by_name('hgjfif'))
