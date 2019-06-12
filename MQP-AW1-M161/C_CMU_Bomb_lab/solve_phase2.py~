### Python script to solve Phase 2 of CMU bomb lab ###

## Bomb lab binary available at https://github.com/yyqian/csapp-labs/blob/master/bomblab/bomb.tar

import angr, monkeyhex, logging

logging.getLogger('angr').setLevel('DEBUG')

proj = angr.Project('./bomb')
ADDR = proj.loader.main_object.plt['phase_2']

print(ADDR)
