from __future__ import absolute_import
import signal

interrupted = False
def signal_handler(signum, frame):
    global interrupted
    interrupted = True

def interrupt_protect(fn):
    def decorator(*args, **kwargs):
        try:
            global interrupted
            interrupted = False
            previous_handler = signal.signal(signal.SIGINT, signal_handler)

            result = fn(*args, **kwargs)
     
            if interrupted:
                raise KeyboardInterrupt
        finally:
            signal.signal(signal.SIGINT, previous_handler)
            interrupted = False

        return result

    return decorator
