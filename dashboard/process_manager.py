import os

def proc_status():
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    
    for pid in pids:
        filename = os.path.join('/proc', pid, 'cmdline')
        details = open(filename, 'rb').read()
       
        if 'fabric.jar' in details:
            return True

    # nothing found
    return False

def proc_start():
    os.system('sudo sh /home/mc-server-fabric-1/start.sh')

def proc_kill():
    pids = [pid for pid in os.listdir('/proc') if pid.isdigit()]
    
    for pid in pids:
        filename = os.path.join('/proc', pid, 'cmdline')
        details = open(filename, 'rb').read()
       
        if 'fabric.jar' in details:
            # kill pid
            os.system(f"sudo kill {pid}")

            # return success
            return True
    
    # server not running
    return False
def proc_restart():
    proc_kill()

    # wait until server has shutdown
    while proc_status():
        pass

    # now start again
    proc_start()
