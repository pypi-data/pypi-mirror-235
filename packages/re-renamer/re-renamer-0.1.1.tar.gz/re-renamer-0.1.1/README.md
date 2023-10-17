# re-renamer

[RE]name files and folders with [RE]gex.

## Usage

re-renamer works right from your cli. Just provide the path the paths you want to rename...

```bash
$ re-renamer -h
usage: re-renamer [-h] [-f FIND] [-r REPLACE] [-c] [-m] [-x] [-d] [--version]
                [paths ...]

[RE]name FILES and DIRECTORIES using [RE]gex.

positional arguments:
  paths                 paths to rename

options:
  -h, --help            show this help message and exit
  -f FIND, --find FIND  Regular expression search string.
  -r REPLACE, --replace REPLACE
                        Regular expression substitution string.
  -c, --case-sensitive  Enable case-sensitive querying.
  -m, --first-match     Query will only match the first occurrence.
  -x, --ignore-extension
                        Query will ignore file extensions.
  -d, --disable-protection
                        Disable path overwrite protection.
  --version             show program's version number and exit

Copyright 2023 Josh Duncan (joshbduncan.com)
```

## Notes

- re-renamer uses the [Python Regular Expression](https://docs.python.org/3/library/re.html) engine.
