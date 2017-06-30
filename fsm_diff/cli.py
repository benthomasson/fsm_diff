"""
Usage:
    fsm_diff [options] <a> <b>

Options:
    -h, --help        Show this page
    --debug            Show debug logging
    --verbose        Show verbose logging
"""
from docopt import docopt
import logging
import sys
import yaml

logger = logging.getLogger('cli')


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parsed_args = docopt(__doc__, args)
    if parsed_args['--debug']:
        logging.basicConfig(level=logging.DEBUG)
    elif parsed_args['--verbose']:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    with open(parsed_args['<a>']) as f:
        a = yaml.load(f.read())

    with open(parsed_args['<b>']) as f:
        b = yaml.load(f.read())


    a_states = {x['label'] for x in a['states']}
    b_states = {x['label'] for x in b['states']}

    missing_in_a = a_states - b_states
    missing_in_b = b_states - a_states

    if (missing_in_b):
        print "Extra states in a:\n   ", "\n    ".join(list(missing_in_b))

    if (missing_in_a):
        print "Extra states in b:\n   ", "\n    ".join(list(missing_in_a))

    a_transitions = {tuple(sorted(x.items())) for x in a['transitions']}
    b_transitions = {tuple(sorted(x.items())) for x in b['transitions']}

    missing_in_a = a_transitions - b_transitions
    missing_in_b = b_transitions - a_transitions

    if (missing_in_b):
        print "Extra transitions in a:\n   ", "\n    ".join(map(str, missing_in_b))

    if (missing_in_a):
        print "Extra transitions in b:\n   ", "\n    ".join(map(str, missing_in_a))

    return 0
