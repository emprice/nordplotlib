import matplotlib as mpl
from . import install as base_install

def install():
    ''' Sets properties for the PDF variant. This one looks best on
    printed media but is not as pleasant on a computer monitor.
    '''
    base_install()

    # background elements get white color explicitly
    mpl.rcParams['figure.facecolor'] = '#ffffff'
    mpl.rcParams['figure.facecolor'] = '#ffffff'
    mpl.rcParams['axes.facecolor']   = '#ffffff'

    # foreground elements get black color explicitly
    mpl.rcParams['axes.edgecolor']   = '#000000'
    mpl.rcParams['text.color']       = '#000000'
    mpl.rcParams['axes.labelcolor']  = '#000000'
    mpl.rcParams['xtick.color']      = '#000000'
    mpl.rcParams['ytick.color']      = '#000000'

    # larger fonts for better readability
    mpl.rcParams['figure.titlesize'] = 24
    mpl.rcParams['xtick.labelsize']  = 16
    mpl.rcParams['ytick.labelsize']  = 16
    mpl.rcParams['axes.labelsize']   = 20
    mpl.rcParams['axes.titlesize']   = 20
    mpl.rcParams['legend.fontsize']  = 20

    # serif fonts everywhere (text and math)
    mpl.rcParams['text.usetex']      = True
    mpl.rcParams['font.family']      = 'serif'

# globals that may be useful for the user when adding other elements
bgcolor = '#ffffff'
fgcolor = '#000000'

# vim: set ft=python:
