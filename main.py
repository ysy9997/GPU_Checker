from pexpect import pxssh
import json

with open('server.json', 'r') as f:
    cf = json.load(f)

for key in cf.keys():
    print(key)
    s = pxssh.pxssh()
    s.login(cf[key]['host'], cf[key]['user'], bytes(cf[key]['password'], 'utf-8'), port=cf[key]['port'])
    s.sendline('nvidia-smi')
    s.prompt(1)
    line = s.before.decode('utf-8')
    print(line.split('                                                                               ')[0])
    s.logout()
