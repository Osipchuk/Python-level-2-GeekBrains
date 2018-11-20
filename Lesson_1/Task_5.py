import subprocess

args_yan = ['ping', 'yandex.ru']
args_you = ['ping', 'youtube.com']

ping_yan = subprocess.Popen(args_yan, stdout=subprocess.PIPE)
ping_you = subprocess.Popen(args_you, stdout=subprocess.PIPE)

for line in ping_yan.stdout:
    print(line.decode('cp866'))

for line in ping_you.stdout:
    print(line.decode('cp866'))

