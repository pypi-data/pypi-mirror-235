# Download Latest

Download a file only if the remote file has changed.

## Example

```sh
URL='https://download.mozilla.org/?product=firefox-latest-ssl&os=linux64&lang=en-US'
ARCHIVE="firefox.tar.bz2"

dl "$URL" "$ARCHIVE"

if [ -f "$ARCHIVE.new" ]; then
  echo "New version detected"
  tar -xjf "$ARCHIVE"
fi
```

## Install

```sh
pip install download-latest
```

[See the install guide](INSTALL.md) for more information.

## Usage

```
usage: download-latest [ -h | --help ] [OPTIONS] URL [FILE]

Download URL to FILE only if remote file has changed.

positional arguments:
  URL                url to download
  FILE               path to output (deduced if not specified, see below)

options:
  -h, --help         show this help message and exit
  -V, --version      show program's version number and exit
  -n, --dry-run      do not download (default: false)
  -f, --force        do not check for changes (default: false)
  -q, --quiet        suppress output (default: false)
  -v, --verbose      increase output (default: false)
  -c, --color        enable colorized output
  -C, --no-color     disable colorized output
  -p, --progress     enable the progress meter
  -P, --no-progress  disable the progress meter
  --backend BACKEND  how to download (default: auto)

BACKEND can be one of 'auto', 'curl', 'wget', or 'python'. If 'auto' is
selected, 'curl' will be chosen if available, then 'wget', then 'python'.

If the color or progress options are not specified, they are determined
from the TTY.

If FILE is not specified, it will be deduced by the filename part of the
URL. If no filename can be deduce, e.g., https://example.com/, then the
program will exit with an error.

Additional files may be generated:

FILE.new       present when download occured, otherwise absent
FILE.download  in-progress download
```
