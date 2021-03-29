cfg_dir=$HOME/session${DISPLAY}
mkdir -p $cfg_dir
code --user-data-dir $cfg_dir $*
