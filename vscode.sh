cfg_dir=$HOME/.vscode/session${DISPLAY}
mkdir -p $cfg_dir
/snap/code/current/usr/share/code/code --user-data-dir $cfg_dir $*
