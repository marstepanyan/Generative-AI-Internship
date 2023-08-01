from DownloadClasses import ThreadingDownloader, MultiprocessingDownloader


class DownloadManager:
    def __init__(self, max_threads, max_processes):
        self.max_threads = max_threads
        self.max_processes = max_processes
        self.downloads = []
        self.after_download = []

    def download(self, url: str, filename: str):
        how_download = input('Enter how you want to download (for Threading T/for Multiprocessing M): ')

        if how_download == 'T':
            download_obj = ThreadingDownloader(url, filename)
        elif how_download == 'M':
            download_obj = MultiprocessingDownloader(url, filename)
        else:
            print('Not supported')
            return
        self.downloads.append(download_obj)

    def start(self):
        thread_count = 0
        process_count = 0
        for download in self.downloads:
            if isinstance(download, ThreadingDownloader):
                thread_count += 1
                if thread_count > self.max_threads:
                    print(f"max should be {self.max_threads} threads, is {thread_count}")
                    return
            if isinstance(download, MultiprocessingDownloader):
                process_count += 1
                if process_count > self.max_processes:
                    print(f"max should be {self.max_threads} threads, is {process_count}")
                    return

        for download in self.downloads:
            d = download.start_download()
            self.after_download.append(d)

    def wait(self):
        for download in self.after_download:
            download.join()
