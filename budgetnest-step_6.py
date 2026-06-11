# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: BudgetNest
def delete_entry(entry_id, confirm=False):
    if entry_id in _entries:
        if confirm or input(f"Удалить запись {entry_id}? (y/n) ") == "y":
            del _entries[entry_id]
            print("Запись удалена.")
        else:
            print("Удаление отменено пользователем.")
    else:
        print(f"Запись с ID {entry_id} не найдена.")
