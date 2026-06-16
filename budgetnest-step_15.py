# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: BudgetNest
class CommandDispatcher:
    def __init__(self, handlers):
        self.handlers = {cmd.lower(): handler for cmd, handler in handlers.items()}

    def dispatch(self, text_command):
        parts = text_command.strip().split(maxsplit=1)
        if not parts: return None
        cmd_name = parts[0]
        args_str = parts[1] if len(parts) > 1 else ""
        handler = self.handlers.get(cmd_name)
        if handler is None: return f"Unknown command: {cmd_name}"
        try:
            result = handler(args_str)
            if isinstance(result, Exception):
                return str(result)
            return result
        except Exception as e:
            return f"Error executing '{cmd_name}': {e}"

    def register(self, cmd_name, handler):
        self.handlers[cmd_name.lower()] = handler
