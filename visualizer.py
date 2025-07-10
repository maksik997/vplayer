import subprocess


class Cava:
    def __init__(self):
        try:
            self.cava_proc = subprocess.Popen(['cava'])
        except FileNotFoundError:
            print("Cava visualisation not supported.")

    def stop(self):
        self.cava_proc.terminate()
        self.cava_proc.wait()

