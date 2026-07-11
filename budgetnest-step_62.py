# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: BudgetNest
import json, os

def score_categories(categories, goals):
    scores = {}
    for cat in categories:
        s = 0
        if "urgent" in cat.get("tags", []): s += 3
        elif "important" in cat.get("tags", []): s += 2
        elif "nice" in cat.get("tags", []): s += 1
        for g in goals:
            if cat["name"].lower() in g["target"].lower(): s += 4
            if cat["name"] == g["category"]: s += 5
        scores[cat["name"]] = s
    return scores

def print_priority(categories, goals):
    scores = score_categories(categories, goals)
    items = list(scores.items())
    items.sort(key=lambda x: -x[1])
    for name, score in items:
        bar = "#" * min(score, 20) + "." * (20 - min(score, 20))
        print(f"{name:25s} {score:>3d} |{bar}")

def save_scores(categories_path, goals_path):
    with open(categories_path) as f: cats = json.load(f)
    with open(goals_path) as f: gls = json.load(f)
    scores = score_categories(cats, gls)
    out = {"categories": cats, "scores": scores}
    with open("budgetnestscores.json", "w") as f: json.dump(out, f, indent=2)

if __name__ == "__main__":
    print_priority("categories.json", "goals.json")
