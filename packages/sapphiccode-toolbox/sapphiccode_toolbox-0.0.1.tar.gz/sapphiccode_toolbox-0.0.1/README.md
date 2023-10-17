# Cassandra's toolbox

## Installation

I recommend using [pipx](https://github.com/pypa/pipx) to install this project:

```
$ pipx install 'git+https://git.sapphicco.de/SapphicCode/toolbox.git'

  installed package sapphiccode-toolbox 0.0.0.post1.dev0+de0bfa3, installed using Python 3.11.4
  These apps are now globally available
    - ct
done! ✨ 🌟 ✨
```

If you depend on this project I also recommend pinning a specific revision, as this project is WIP and things are very much subject to change.

Additionally, the `image` group of commands optionally require [ExifTool](https://exiftool.org/) and [ImageMagick](https://imagemagick.org/)/[GraphicsMagick](https://www.graphicsmagick.org/).

## Usage

```
Usage: ct [OPTIONS] COMMAND [ARGS]...

  Cassandra's toolbox

  A bunch of utilities that probably don't mean anything to anyone else.

Options:
  --log-level TEXT     Sets the log level for toolbox.  [default: INFO]
  --log-level-tp TEXT  Sets the log level for third-party loggers.  [default:
                       INFO]
  --help               Show this message and exit.

Commands:
  image  Image manipulation commands
```
