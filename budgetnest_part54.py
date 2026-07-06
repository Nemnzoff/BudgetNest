# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: BudgetNest
def colorize(text, color):
    """Return text wrapped in ANSI color codes for terminal output."""
    colors = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'cyan': '\033[96m',
        'magenta': '\033[95m',
        'white': '\033[97m',
        'bold': '\033[1m',
        'reset': '\033[0m',
    }
    if color not in colors:
        return text
    return f"{colors[color]}{text}{colors['reset']}"

def money(amount):
    """Return a formatted, colorized monetary string."""
    sign = '+' if amount >= 0 else '-'
    return colorize(f" {sign}{amount:.2f}", 'green' if amount >= 0 else 'red')
