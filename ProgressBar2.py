# To test these progress bars you will have to
# install the following packages
# pipenv install click progress progressbar2 tqdm clint

import string

# progress bars
import time
import click
from tqdm import tqdm
from progress.bar import Bar
from progress.bar import PixelBar
from progress.spinner import PixelSpinner
from progressbar import progressbar
from clint.textui import progress

click.secho('Progress - BAR', bold=True)
with Bar('Processing...') as bar:
    for i in range(100):
        time.sleep(0.02)
        bar.next()

click.secho('Progress - PixelBar', bold=True)
with PixelBar('Processing...') as bar:
    for i in range(100):
        time.sleep(0.02)
        bar.next()

click.secho('Progress - PixelSpinner', bold=True)
with PixelSpinner('Processing...') as bar:
    for i in range(100):
        time.sleep(0.02)
        bar.next()

click.secho('\nProgressbar2', bold=True)
for i in progressbar(range(100), redirect_stdout=True):
    time.sleep(0.02)

click.secho('\nTQDM', bold=True)
for i in tqdm(range(100)):
    time.sleep(0.02)

click.secho('TQDM - With description', bold=True)
pbar = tqdm(list(string.ascii_lowercase))
for letter in pbar:
    pbar.set_description(f'Processing {letter}...')
    time.sleep(0.09)

click.secho('\nClick', bold=True)
fill_char = click.style('=', fg='yellow')
with click.progressbar(range(100), label='Loading...', fill_char=fill_char) as bar:
    for i in bar:
        time.sleep(0.02)

click.secho('\nClint', bold=True)
for i in progress.bar(range(100)):
    time.sleep(0.02)

click.secho('Clint - Mill', bold=True)
for i in progress.mill(range(100)):
    time.sleep(0.02)
