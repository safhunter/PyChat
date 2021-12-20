import subprocess
import chardet


args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
char_enc = 'utf-8'
try:
    for num, line in enumerate(subproc_ping.stdout):
        char_enc = chardet.detect(line)['encoding']
        decoded_line = line.decode(char_enc)
        print(f'{decoded_line}')
except (UnicodeEncodeError, SyntaxError):
    print(f'Decode error')

args = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
char_enc = 'utf-8'
try:
    for num, line in enumerate(subproc_ping.stdout):
        char_enc = chardet.detect(line)['encoding']
        decoded_line = line.decode(char_enc)
        print(f'{decoded_line}')
except (UnicodeEncodeError, SyntaxError):
    print(f'Decode error')
