import matplotlib as mpl
from . import install as base_install

def install():
    ''' Sets properties for the PNG variant. This one looks best on
    a computer monitor but would not be appropriate for journal submission.
    '''
    base_install()

    # background elements get a dark color (replacing white)
    mpl.rcParams['figure.facecolor']    = '#2e3440'
    mpl.rcParams['figure.facecolor']    = '#2e3440'
    mpl.rcParams['axes.facecolor']      = '#2e3440'

    # foreground elements get a light color (replacing black)
    mpl.rcParams['axes.edgecolor']      = '#eceff4'
    mpl.rcParams['text.color']          = '#eceff4'
    mpl.rcParams['axes.labelcolor']     = '#eceff4'
    mpl.rcParams['xtick.color']         = '#eceff4'
    mpl.rcParams['ytick.color']         = '#eceff4'

    # larger fonts for better readability
    mpl.rcParams['figure.titlesize']    = 24
    mpl.rcParams['xtick.labelsize']     = 16
    mpl.rcParams['ytick.labelsize']     = 16
    mpl.rcParams['axes.labelsize']      = 20
    mpl.rcParams['axes.titlesize']      = 22
    mpl.rcParams['legend.fontsize']     = 20

    # sans-serif math that looks really nice (though latex does take
    # a bit longer to render, since it has to compile first)
    mpl.rcParams['text.usetex']         = True
    mpl.rcParams['font.family']         = 'sans-serif'
    mpl.rcParams['text.latex.preamble'] = \
        '\n'.join([r'\usepackage{cmbright}',
                   r'\usepackage[OT1]{fontenc}',
                   r'\usepackage{amsmath}'])

# globals that may be useful for the user when adding other elements
bgcolor = '#2e3440'
fgcolor = '#eceff4'

# vim: set ft=python:
