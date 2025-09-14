from datetime import datetime, timedelta


def date_range(start_date, end_date):
    """
    Возвращает список дат за период от start_date до end_date включительно.

    Args:
        start_date (str): начальная дата в формате YYYY-MM-DD
        end_date (str): конечная дата в формате YYYY-MM-DD

    Returns:
        list: список строк с датами в формате YYYY-MM-DD
    """
    try:
        # Преобразуем строки в объекты datetime
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")

        # Проверяем, что start_date <= end_date
        if start > end:
            return []

        # Создаем список дат
        date_list = []
        current_date = start

        while current_date <= end:
            date_list.append(current_date.strftime("%Y-%m-%d"))
            current_date += timedelta(days=1)

        return date_list

    except ValueError:
        # Если формат дат неверный
        return []
