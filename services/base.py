import time


class Base:
    BASE_URL = "https://petstore.swagger.io"

    def wait_for_status(func, expected_status=200, timeout=5, interval=0.5, max_retries=10, *args, **kwargs):
        """
        Вызывает функцию func(*args, **kwargs) до тех пор, пока её ответ не вернёт expected_status
        или не выйдет таймаут или лимит повторов.

        :param func: функция, которая возвращает Response
        :param expected_status: ожидаемый HTTP код
        :param timeout: максимальное время ожидания в секундах
        :param interval: пауза между попытками в секундах
        :param max_retries: максимальное количество попыток
        :param args: позиционные аргументы для func
        :param kwargs: именованные аргументы для func
        :return: Response с expected_status
        :raises Exception: если статус не достигнут за timeout или max_retries
        """
        start_time = time.time()
        retries = 0
        while time.time() - start_time < timeout and retries < max_retries:
            response = func(*args, **kwargs)
            if response.status_code == expected_status:
                return response
            retries += 1
            time.sleep(interval)
        raise Exception(
            f"{func.__name__} did not return {expected_status} within {timeout} seconds "
            f"after {retries} retries"
        )