"""
Things for printing messages.
"""


def cprint(s, *msg_types, indent=0):
    """Print things with colors."""

    # Right now, this only works with foreground colors and styles

    # Get ANSI escape sequence from colors class or styles class
    # Default to empty string if invalid
    valid_ansi = [getattr(colors.fg, t, getattr(styles, t, ""))
                  for t in msg_types
                  ]

    # If there were no valid styles (the styles list is empty), then we don"t
    # need to add a reset to the end of our print statement
    end = colors.end if valid_ansi else ""

    indent = "    " * indent

    print("".join(valid_ansi) + indent + s + end)


class _ansi_global:
    end = "\033[0m"


class colors(_ansi_global):
    class fg:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        yellow = "\033[33m"
        blue = "\033[34m"
        magenta = "\033[35m"
        cyan = "\033[36m"
        white = "\033[37m"

    class bg:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        yellow = "\033[43m"
        blue = "\033[44m"
        magenta = "\033[45m"
        cyan = "\033[46m"
        white = "\033[47m"


class styles(_ansi_global):
    bold = "\033[1m"
    underline = "\033[4m"

