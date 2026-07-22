# === Stage 83: Add regression tests for the final demo workflow ===
# Project: BudgetNest
import os, json

PROJECT = os.path.join(os.environ.get("HOME","/tmp"), "budgetnest")
os.makedirs(PROJECT, exist_ok=True)

# --- helpers that mirror the main app (no external deps) ---

def load(path): return json.load(open(path)) if path else {}
def save(path, data): open(path,"w").write(json.dumps(data, indent=2))

def add_entry(db, cat, amt, note=""):
    db.setdefault("entries",[]).append({"cat":cat,"amt":float(amt),"note":note})
    return db

def calc_balance(db):
    bal = 0.0
    for e in db.get("entries",[]):
        try: val = float(e["amt"]); sign = -1 if e["cat"].startswith(("Food","Rent","Utilities","Insurance")) else 1; bal += sign*val
        except: pass
    return round(bal,2)

def goals_met(db):
    total_spent = sum(float(e["amt"]) for e in db.get("entries",[]) if float(e["amt"])>0)
    g_list = db.get("goals",[])
    return [g for g in g_list if g.get("target",0)>=total_spent]

def gen_report(db):
    entries = db.get("entries",[])
    lines = ["BudgetNest Report\n"]
    cat_totals = {}
    for e in entries:
        c, a = e["cat"], round(float(e["amt"]),2)
        cat_totals[c] = cat_totals.get(c,0)+a
    for c,a in sorted(cat_totals.items(), key=lambda x:-abs(x[1])):
        lines.append(f"  {c}: ${a:+,.2f}")
    bal = calc_balance(db)
    goals = goals_met(db)
    if goals: lines.append(f"\nGoals met: {len(goals)}")
    return "\n".join(lines)

# --- demo workflow (driven by a JSON file, no prompt needed) ---

def run_demo_workflow():
    with open(os.path.join(PROJECT,"demo_input.json")) as f:
        cfg = json.load(f)
    db = {"entries":[], "goals":[]}
    for rec in cfg.get("recurring",[]):
        add_entry(db, rec["cat"], rec["amt"])
    for item in cfg.get("items",[]):
        add_entry(db, item["cat"], item["amt"], item.get("note",""))
    save(os.path.join(PROJECT,"budget.json"), db)
    report = gen_report(db)
    print(report)

try: run_demo_workflow()
except FileNotFoundError as e:
    print(f"demo_input.json missing; create it then re-run")
