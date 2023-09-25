from modules.record import SoundRecorder
from modules.window import WindowCanvasManager
from queue import Queue
from threading import Thread
import sys
import signal


def safe_exit(signum, frame):
    print("Exiting gracefully...")
    sys.exit(0)


if __name__ == "__main__":
    voice_angle_queue = Queue()

    # キーボード割り込みを処理するための設定
    signal.signal(signal.SIGINT, safe_exit)

    recoder = SoundRecorder(voice_angle_queue)
    recoder.start_recording()

    window = WindowCanvasManager()
    drow_voice_angle_arc_and_text_forever_thread = Thread(
        target=window.draw_voice_angle_arc_and_text_forever,
        args=(voice_angle_queue),
    )
    drow_voice_angle_arc_and_text_forever_thread.start()

    try:
        window.run()
    except KeyboardInterrupt:
        safe_exit(None, None)
