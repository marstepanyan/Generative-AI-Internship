from abc import ABC, abstractmethod
import requests
import threading
import multiprocessing
from urllib.parse import urlparse
from ftplib import FTP
from io import BytesIO


class Download(ABC):
    def __init__(self, url, filename):
        self.url = url
        self.filename = filename

    @abstractmethod
    def start_download(self):
        raise NotImplementedError("Subclasses must implement start_download() method.")

    def save_file(self, content: bytes):
        with open(self.filename, "wb") as file:
            file.write(content)

    def download_complete(self):
        print(f"Download of {self.url} is complete.")


class ThreadingDownloader(Download):
    def start_download(self):
        thread = threading.Thread(target=self._download_with_threading)
        thread.start()
        return thread

    def _download_with_threading(self):
        content = download_file(self.url)
        if content:
            self.save_file(content)
        self.download_complete()


class MultiprocessingDownloader(Download):
    def start_download(self):
        process = multiprocessing.Process(target=self._download_with_multiprocessing)
        process.start()
        return process

    def _download_with_multiprocessing(self):
        content = download_file(self.url)
        if content:
            self.save_file(content)
        self.download_complete()


def download_file(url: str) -> bytes:
    if url.startswith('http://') or url.startswith('https://'):
        response = requests.get(url)
        return response.content
    elif url.startswith('ftp://'):
        parsed_url = urlparse(url)
        host = parsed_url.hostname
        path = parsed_url.path

        with FTP(host) as ftp:
            ftp.login()
            ftp.cwd('/')
            with BytesIO() as file_buffer:
                ftp.retrbinary(f"RETR {path}", file_buffer.write)
                return file_buffer.getvalue()
    else:
        raise ValueError("Unsupported URL scheme. Only HTTP, HTTPS, and FTP URLs are supported.")
