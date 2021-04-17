import itertools
import threading
import sys


def animate(stop_event):
    sys.stdout.write('\n\n')
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if stop_event.wait(0.1):
            break
        sys.stdout.write('\rLoading     [' + c + ']')
        sys.stdout.flush()
    sys.stdout.write('\rDone!     ')


stop_thread_event = threading.Event()

loading_animation_thread = threading.Thread(
    target=animate, args=(stop_thread_event,))


def stop_loading_animation_thread():
    stop_thread_event.set()
    loading_animation_thread.join()
