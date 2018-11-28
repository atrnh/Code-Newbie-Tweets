"""
Things for printing messages.
"""


def cprint(s, *msg_types, indent=0):
    styles = [getattr(colors, t, '') for t in msg_types]
    end = colors.ENDC if msg_types else ''
    indent = ' ' * indent

    print(''.join(styles) +
          indent +
          s +
          end
          )


class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
