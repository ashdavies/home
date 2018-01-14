import subprocess32
import re

host = 'jetbrains.com'
ping_output = subprocess32.check_output(["ping", host, "-c 5"])

for line in ping_output.split('\n'):
    if re.match("\d+ bytes from", line):
        print(line)
