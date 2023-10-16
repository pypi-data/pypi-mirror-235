"""
pyPreservica.Gov auto run module

author:     James Carr
licence:    Apache License 2.0

"""
import sys

from pyPreservicaGov import PreservicaGov
from pyPreservicaGov import Schema
import signal
import readchar


class StopScriptCallback:

    def __init__(self):
        self.stop = False

    def stop_script(self):
        self.stop = True

    def __call__(self):
        return self.stop


stopCallback = StopScriptCallback()


def handler(signum, frame):
    msg = "Ctrl-c was pressed. Do you really want to exit? y/n "
    print(msg, end="", flush=True)
    res = readchar.readchar()
    if res == 'y':
        print("")
        stopCallback.stop_script()
        exit(1)
    else:
        print("", end="\r", flush=True)
        print(" " * len(msg), end="", flush=True)
        print("    ", end="\r", flush=True)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handler)

    # Load the Schemas and Transforms
    schema = Schema()
    schema.load_schema()
    schema.load_indexes()
    schema.load_cmis()

    # Run the harvest
    preservica = PreservicaGov(callback=None, stopCallback=stopCallback)
    preservica.harvest()
