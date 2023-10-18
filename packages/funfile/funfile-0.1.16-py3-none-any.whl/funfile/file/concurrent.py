import time
from queue import Queue
from threading import Thread


class ConcurrentFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.writeQueue = Queue()
        self._close = False
        thread = Thread(target=self._write)
        thread.start()

    def add_chunk(self, offset, chunk):
        self.writeQueue.put((offset, chunk))

    def _write(self):
        with open(self.filepath, 'w') as fw:
            chunk_size = 0
            while True:
                try:
                    offset, chunk = self.writeQueue.get()
                    fw.seek(offset)
                    fw.write(chunk)
                    chunk_size += len(chunk)
                    if chunk_size > 10 * 1024 * 1024:
                        fw.flush()
                        chunk_size = 0
                    self.writeQueue.task_done()
                except Exception as e:
                    pass
                if self._close:
                    break

    def close(self):
        self._close = True

    def wait_for_all_done(self):
        self.writeQueue.join()

    def empty(self):
        return self.writeQueue.empty()


class FileOpen(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self._handle = None  # type: ConcurrentFile

    def __enter__(self):
        self._handle = ConcurrentFile(filepath=self.filepath)
        return self._handle

    def __exit__(self, exc_type, exc_val, exc_tb):
        while not self._handle.empty():
            time.sleep(1)
        self._handle.wait_for_all_done()
        self._handle.close()
        return True
