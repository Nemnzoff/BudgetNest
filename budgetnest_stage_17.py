# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: BudgetNest
def dry_run_mode():
    import sys, argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    
    if args.dry_run:
        print("DRY RUN MODE ENABLED")
        
        def log_action(action):
            print(f"[DRY] {action}")
            
        original_print = print
        
        class DryRunLogger:
            pass
            
        sys.stdout.write = lambda s, *args, **kwargs: (log_action(s) or None) if args.dry_run else original_print(*args, **kwargs)
        
    return args.dry_run
