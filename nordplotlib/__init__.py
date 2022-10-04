import cycler
import matplotlib as mpl
from collections import namedtuple

__version__ = '2022.10.04.dev1'

NordColors = namedtuple('NordColors', ['red', 'orange', 'yellow',
    'green', 'greenish', 'lightblue', 'blue', 'darkblue', 'purple'])
colors = NordColors(red='#bf616a', orange='#d08770', yellow='#ebcb8b',
    green='#a3be8c', greenish='#8fbcbb', lightblue='#88c0d0',
    blue='#81a1c1', darkblue='#5e81ac', purple='#b48ead')

def install():
    ''' Sets properties common to all variants.
    '''
    # colors used for lines on plots
    color_cycle = [colors.red, colors.greenish, colors.orange,
                   colors.lightblue, colors.yellow, colors.blue,
                   colors.green, colors.darkblue, colors.purple]
    mpl.rcParams['axes.prop_cycle'] = cycler.cycler('color', color_cycle)

    # interactively save figures in the current (not home) directory
    mpl.rcParams['savefig.directory'] = ''

    # a simple default figure size
    mpl.rcParams['figure.figsize'] = (8, 6)

    # spine ticks go inward (more consistent with journal standards)
    mpl.rcParams['xtick.direction'] = 'in'
    mpl.rcParams['ytick.direction'] = 'in'

    # add a little padding around the ticks
    mpl.rcParams['xtick.major.pad'] = 8
    mpl.rcParams['ytick.major.pad'] = 8

# vim: set ft=python:
