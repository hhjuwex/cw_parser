from datetime import datetime, timedelta

dates = {
    "января": '01',
    "февраля": '02',
    "марта": '03',
    "апреля": '04',
    "мая": '05',
    "июня": '06',
    "июля": '07',
    "августа": '08',
    "сентября": '09',
    "октября": '10',
    "ноября": '11',
    "декабря": '12'
}


def parsing_metadata(report: list) -> dict:
    metadata = report[0].split()
    report_id = metadata[0]
    date = ''
    match metadata[1]:
        case "Вчера":
            date = f'{metadata[3]} {(datetime.now() - timedelta(days=1)).strftime("%d.%m.%Y")}'
        case "Сегодня":
            date = f'{metadata[3]} {datetime.now().strftime("%d.%m.%Y")}'
    if not date:
        day = '0' + metadata[1] if len(metadata[1]) == 1 else metadata[1]
        month = dates[metadata[2]]
        year = datetime.now().year if metadata[3] == 'в' else metadata[3]
        date = f'{metadata[4] if metadata[4] != 'в' else metadata[5]} {day}.{month}.{year}'

    i = metadata.index('@') + 1
    name = ''
    while i < len(metadata):
        name += metadata[i] + ' '
        if 'Жалоба' in metadata[i] or 'Удалить' in metadata[i]: break
        i += 1

    i = name.index('Жалоба') if 'Жалоба' in name else name.index('Удалить')
    name = name[:i]
    metadata_report = {
        'report_id': report_id,
        'author': name,
        'report_date': date
    }

    return metadata_report


