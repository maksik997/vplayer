# VPlayer

**Version: 1.0**

---

## Description

VPlayer is a sleek media player featuring audio visualization capabilities. It provides a modern way to enjoy your media files along with real-time audiovisual effects.

**Please note:** I'm nothing more than python newbie and this particular application is just adaptation of my simple bash script to play music visually.

## Requirements

Before installing and running VPlayer, make sure you have the following dependencies installed on your system:

- [`cava`](https://github.com/karlstav/cava) — for audio visualization
- [`vlc`](https://www.videolan.org/vlc/) — media playback backend

## Installation

You can install VPlayer either from source or by using prebuilt binaries.

### 1. Installation from Source

Follow these steps to build and install VPlayer manually:

1. Clone the repository:

```bash
git clone git@github.com:maksik997/vplayer.git
cd vplayer
```

2. Create and activate a Python virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install `pyinstaller` inside the virtual environment:

```bash
pip install pyinstaller 
```

4. Build the executable with PyInstaller:

```bash
pyinstaller --name=vplayer --onefile --specpath=. --noparse vplayer.py
```
>**Note:** Adjust the paths `/usr/lib64/vlc/libvlc.so` and `/usr/lib64/vlc/libvlccore.so` to your system’s VLC library locations.
> Or just specified them in `.spec` file.

### 2. Using prebuild binaries

- Navigate to [releases](https://github.com/maksik997/vplayer/releases) section of this repository.
- Download the latest binary suitable for your operating system.
- Extract and run the executable directly.

## Troubleshooting

If you encounter issues related to VLC plugin paths or missing libraries, try setting the following environment variable:
```bash
export VLC_PLUGIN_PATH="/usr/lib64/vlc/plugins"
```
Make sure the path points to where VLC plugins are installed on your system.

For PyInstaller, you might need to explicitly include VLC binaries in the `vplayer.spec` file to ensure proper packaging.

Adding to `*.spec` binaries with vlc libs.

## Usage

Run VPlayer from the command line as follows:
```bash
vplayer <file1> [file2 ...]
```

To display help and available options:
```bash
vplayer --help
```

## License

Project is licensed under MIT License available under [LICENSE](https://github.com/maksik997/vplayer/blob/main/LICENSE) file.

## Contributing

Feel free to fork the project and submit pull requests. Issues and feature requests are also welcome.

## Contact 

For questions or support, please open an issue on GitHub

---

_Enjoy your music with VPlayer!_
