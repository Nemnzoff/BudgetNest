# === Stage 31: Add compact table rendering for long lists ===
# Project: BudgetNest
def render_compact_table(headers, rows):
    if not headers: return ""
    col_widths = [max(len(str(h)), max((len(str(r)) for r in row), default=0)) for h, row in zip(headers, rows)]
    header_line = "  ".join(f"{h:<{col_widths[i]}}" for i, h in enumerate(headers))
    sep_line = "-".join("-" * col_widths[i] for i in range(len(headers)))
    body_lines = []
    for row in rows:
        line = "  ".join(str(r) if r is not None else "-" for r in row)
        body_lines.append(line[:len(sep_line)])
    return header_line + "\n" + sep_line + "\n" + "\n".join(body_lines)
