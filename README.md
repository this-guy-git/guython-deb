# Guython Debian
Guython as a Debian package for Debian/Ubuntu.

# Install with 1 line cmd
wget "$(curl -s https://api.github.com/repos/this-guy-git/guython-deb/releases/latest | grep browser_download_url | grep .deb | cut -d '"' -f 4)" -O guython.deb && sudo dpkg -i guython.deb

# Install with GUI
Install the .deb from the releases

Navigate to the directory where installed

Run 'sudo dpkg -i guython-deb{VER}.deb' where {VER} is the current version

Run 'guython' or 'guython {file}.gy'

# Install with CLI
Use 'wget https://github.com/this-guy-git/guython-deb/releases/download/v{TAG}/guython-deb.deb' where {VER} and {TAG} is the version you wish to download
- Latest release 'wget "$(curl -s https://api.github.com/repos/this-guy-git/guython-deb/releases/latest | grep browser_download_url | grep .deb | cut -d '"' -f 4)" -O guython.deb && sudo dpkg -i guython.deb'

Run 'sudo dpkg -i guython-deb{VER}.deb' where {VER} is the installed version

Run 'guython' or 'guython {file}.gy'
