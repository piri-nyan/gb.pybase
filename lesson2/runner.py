import os

files = os.listdir(os.path.dirname(__file__)+'\\\\tasks')
for file in files:
    if 'task' in file:
        print("="*10+file+"="*10)
        with open(os.path.dirname(__file__)+'/tasks/'+file) as runnable:
            exec(runnable.read())