# VPlayer

**Version: 1.0**

---

## Description

Fancy media player with audio visualization.

## Requirements

`cava`, `vlc`

## Installation

...
1. From source
    - Clone this repo
    - Activate venv
    - Install pyinstaller
    - Build
    - If build fails, add libvlc* libraries
2. Binaries
   - Go to releases section
   - Download, then start.

## Troubleshooting

Adding to `*.spec` binaries with vlc libs.

`export VLC_PLUGIN_PATH = "/usr/lib64/vlc/plugins"`

## Usage

`vplayer <file> [file...]`

`vplayer --help` for help
