conda install -y jproperties typer

mkdir -p ~/bin/
cp -af run_idea.py gchrome.sh vscode.sh ~/bin/
cp -ar Desktop/*.desktop ~/Desktop/
mkdir -p ~/.idea
cp -ar idea/* ~/.idea/
