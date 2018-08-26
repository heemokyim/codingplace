import psutil
from subprocess import Popen, PIPE
import pickle

def bring_me_password(path='YOUR/PATH/TO/PASSWORD'):
    with open(path, 'rb') as f:
        pw = pickle.load(f)
    return pw + '\n'

def teamviewer_stop():
    teamviewer_shell('stop')

def teamviewer_start():
    if not is_teamviewer_running():
        teamviewer_shell('start')

def teamviewer_restart():
    teamviewer_shell('restart')

def teamviewer_shell(mode='restart'):
    command = ['sudo', '-S', 'service', 'teamviewerd', mode]
    proc = Popen(command, stdin=PIPE, stdout=PIPE)
    proc.communicate(str.encode(bring_me_password()))

def is_teamviewer_running():
    ps_list = [each.name() for each in psutil.process_iter()]
    if 'TeamViewer' in ps_list:
        return True
    return False

if __name__ == '__main__':
    teamviewer_start()