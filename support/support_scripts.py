"""Небольшие вспомогательные скрипты"""
from flask import abort




def booking_link_checker(path, teachers):
    """Проверяет корректность URL"""
    to_check_list = path.split('/')[-4:]
    id = int(to_check_list[0])
    weekDay = to_check_list[1]
    time = to_check_list[2]

    teachers_id_range = [i for i in range(len(teachers))]

    if id in teachers_id_range:
        days_range = teachers[id]['free'].keys()
        if weekDay in days_range:
            times_range = teachers[id]['free'][weekDay].keys()
            if time in times_range:
                return True
    abort(404)
