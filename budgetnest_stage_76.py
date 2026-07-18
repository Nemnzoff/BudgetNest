# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: BudgetNest
import sys, os, signal as _sig

def _handle_sigint(_signum, frame):
    """Gracefully stop the CLI on ^C."""
    print("\nBudgetNest: interrupted — shutting down cleanly.")
    sys.exit(0)


# Register handlers once before any CLI invocation.
for sig in (_sig.SIGINT,):
    try:
        _sig.signal(sig, _handle_sigint)
    except (ValueError, OSError):
        pass  # already handled or not supported on this platform
