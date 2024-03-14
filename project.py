import subprocess

login_process = subprocess.Popen(['python', 'login.py'])
login_process.communicate()

print('welcome')

def kill_process(process):
    try:
        process.terminate() 
    except OSError:
        pass  

# Launch the first program
quiz_process = subprocess.Popen(['python', 'quiz.py'])

# Launch the second program
mp_process = subprocess.Popen(['python', 'mp.py'])

face_check = subprocess.Popen(['python', 'face_check.py'])

quiz_process.wait()

# If the first process terminates, terminate the second process
kill_process(mp_process)
kill_process(face_check)