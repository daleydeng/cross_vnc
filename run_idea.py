#!/usr/bin/env python
import os
import os.path as osp
import sys
import shutil
from jproperties import Properties

def process_ide(ide, exe=None):
    if exe is None:
        exe = ide

    display = os.environ['DISPLAY']
    cfg_dir = osp.expanduser(f'~/.idea/{ide}/session{display}')
    os.makedirs(cfg_dir, exist_ok=True)

    bin_path = shutil.which(exe)
    ide_bin_dir = osp.abspath(osp.dirname(bin_path) + f'/../{exe}/current/bin/')
    prop_f =  ide_bin_dir + '/idea.properties'
    prop = Properties()
    prop.load(open(prop_f, 'rb'))
    prop.update({
        "idea.config.path":  cfg_dir + '/config',
        'idea.system.path': cfg_dir + '/system',
    })

    o_prop_f = cfg_dir + '/idea.properties'
    prop.store(open(o_prop_f, 'wb'))

    sh_f = f'{ide_bin_dir}/{ide}.sh'
    assert osp.exists(sh_f), f"{sh_f} not exists"
    cmd = f'{ide.upper()}_PROPERTIES={o_prop_f} {sh_f}'
    print (cmd)
    os.system(cmd)

def main(ide):
    ide = ide.lower()
    if ide == 'clion':
        process_ide('clion')
    elif ide == 'pycharm':
        process_ide('pycharm', 'pycharm-professional')
    elif ide == 'webstorm':
        process_ide('webstorm')
    else:
        raise RuntimeError(f"{ide} not found")

if __name__ == "__main__":
    import typer
    typer.run(main)
