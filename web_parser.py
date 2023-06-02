import requests


class WebParser:
    def __init__(self, url):
        self.url = url

    def get_page_text(self) -> str:
        """Функция для получения текста страницы.
        Возвращает текст страницы."""
        response = requests.get(self.url)
        page_content = response.content
        page_content = str(page_content)
        return page_content
