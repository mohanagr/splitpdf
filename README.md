# splitpdf
Split a PDF in colored and b/w parts to optimize your printing expenditure. Code written in 5 minutes, don't sue me if you pay more than what it estimated.

# Requirements

`sudo apt install ghostscript`

`sudo apt install pdftk`

Uses a default python version installed in `/usr/bin/`. Change the first line (hashbang) for your python version if 3.6.8 is not present.

# Running

```./splitpdf /path/to/file.pdf [-n]```

`-n` option will only give total counts and page numbers. On not using this option the PDFs will be dumped to current directory.

