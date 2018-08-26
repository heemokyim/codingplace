import psutil
from subprocess import Popen, PIPE
import pickle

def bring_me_password(path='../tmp'):
    with open(path, 'rb') as f:
        pw = pickle.load(f)
    return pw + '\n'

def teamviewer_stop():
    teamviewer('stop')

def teamviewer_start():
    teamviewer('start')

def teamviewer_restart():
    teamviewer('restart')

def teamviewer(mode='restart'):
    for each in psutil.process_iter():
        if 'TeamViewer' in each.name():
            break
        else:
            command = ['sudo', '-S', 'service', 'teamviewerd', mode]
            proc = Popen(command, stdin=PIPE, stdout=PIPE)
            proc.communicate(str.encode(bring_me_password()))
            break

if __name__ == '__main__':
    teamviewer_restart()