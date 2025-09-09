import logging
import time
from datetime import datetime, timezone

import requests


class Base:
    logger = logging.getLogger("API")

    BASE_URL = "https://petstore.swagger.io"

    def wait_for_status(
        func,
        expected_status=200,
        timeout=5,
        interval=0.5,
        max_retries=10,
        *args,
        **kwargs,
    ):
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
    

    @classmethod
    def post(cls, url, json=None, files=None):
        "Sending POST request to url: " + url
        cls.logger.info(f"Sending POST request to url:  {url}")
        response = requests.post(url, json=json, files=files)
        cls.logger.debug(f"Response status code[{response.status_code}] {response.text}")
        cls.logger.debug(f"Response body {response.text}")
        return response

    @classmethod
    def get(cls, url, params=None):
        cls.logger.info(f"Sending GET request to url: {url}")
        response = requests.get(url, params=params)
        cls.logger.debug(f"Response status code[{response.status_code}]")
        cls.logger.debug(f"Response body  {response.text}")
        return response

    @classmethod
    def put(cls, url, json=None):
        cls.logger.info(f"Sending PUT request to url: {url}")
        response = requests.put(url, json=json)
        cls.logger.debug(f"Response status code =  [{response.status_code}]")
        cls.logger.debug(f"Response body  {response.text}")
        return response

    @classmethod
    def delete(cls, url):
        cls.logger.info(f"Sending DELETE request to url: {url}")
        response = requests.delete(url)
        cls.logger.debug(f"Response status code[{response.status_code}]")
        cls.logger.debug(f"Response body  {response.text}")
        return response
    
    @staticmethod
    def check_response_status_code(response, status_code):
        assert response.status_code == status_code, f"Ожидаемый статус: [{status_code}] | Актуальный: [{response.status_code}]"
