import threading
import pyttsx3
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
 
def do_something_and_move_on():
    pass
 
worker = threading.Thread(target=do_something_and_move_on)
worker.start()
 
# now do other things while it runs...
 
# then join the worker, to make sure it's done before the script ends
worker.join()
 
def talk(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()
    engine.stop()
    return 'done'
 
 
executor = ThreadPoolExecutor(max_workers=20) 
future = executor.submit(talk('This will be, a long text for testing purpose.'))
future = executor.submit(talk('OK, Fuck you asshole.'))
print('This text should appear before or during the TTS')
#print(future.result())