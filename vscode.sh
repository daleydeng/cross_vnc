cfg_dir=$HOME/.vscode/session${DISPLAY}
mkdir -p $cfg_dir
code --user-data-dir $cfg_dir $*
