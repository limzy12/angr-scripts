import angr, monkeyhex, binascii

proj = angr.Project('./testing')
simgr = proj.factory.simgr()

simgr.explore(find = lambda s: b'Success!' in s.posix.dumps(1))

s = simgr.found[0]

print(s.posix.dumps[1])
number = s.posix.dumps[0]
print(number)
