import mss
import numpy as np
import subprocess
import threading
import os
from datetime import datetime

class Recorder:
    def __init__(self):
        self.running = False
        self.proc = None

    def start(self, fps=60, quality="high"):
        os.makedirs("recordings", exist_ok=True)

        file = f"recordings/gamer_{datetime.now().strftime('%H%M%S')}.mp4"

        monitor = mss.mss().monitors[1]
        w, h = monitor["width"], monitor["height"]

        crf = "18" if quality == "high" else "28"

        cmd = [
            "ffmpeg",
            "-y",
            "-f", "rawvideo",
            "-pix_fmt", "bgr0",
            "-s", f"{w}x{h}",
            "-r", str(fps),
            "-i", "-",
            "-c:v", "libx264",
            "-preset", "ultrafast",
            "-crf", crf,
            "-pix_fmt", "yuv420p",
            file
        ]

        self.proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
        self.running = True

        def loop():
            with mss.mss() as sct:
                while self.running:
                    frame = np.array(sct.grab(monitor))
                    self.proc.stdin.write(frame.tobytes())

        threading.Thread(target=loop, daemon=True).start()

    def stop(self):
        self.running = False
        if self.proc:
            self.proc.stdin.close()
            self.proc.wait()