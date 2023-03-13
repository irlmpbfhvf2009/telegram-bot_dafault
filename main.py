from multiprocessing import freeze_support, Process
from src.gui.__init__ import App as Gui


if __name__ == "__main__":
    freeze_support()    
    windowProcess = Process(target=Gui().run())
    windowProcess.start()
    windowProcess.join()