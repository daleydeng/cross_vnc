if [ ! -f /etc/yum.repos.d/google-chrome.repo ]; then
    cp etc/yum.repos.d/google-chrome.repo /etc/yum.repos.d/
fi
dnf install -y google-chrome-stable
snap install clion --classic
snap install pycharm-professional --classic
snap install webstorm --classic
snap install code
