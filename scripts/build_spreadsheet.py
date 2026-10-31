#!/usr/bin/env python3
"""Build the job-hunt workbook from a JSON file.

Usage: python3 build_spreadsheet.py data.json AI_Job_Outreach_Nov2026.xlsx

data.json keys (each a list of objects whose keys match the column names
below, lowercased with underscores): shortlist, instagram_vs_linkedin,
more_instagram_finds, requirements_check, excluded, notes.
"""
import json
import sys

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill

TABS = {
    "Shortlist": [
        "Priority", "Company", "Role", "Location", "Work mode",
        "Experience asked", "Fit", "LinkedIn status", "LinkedIn link",
        "Contact email", "Email source", "Apply method", "Status", "Notes",
    ],
    "Instagram vs LinkedIn": [
        "Company", "Role", "Instagram post date", "Instagram experience",
        "LinkedIn status", "LinkedIn experience", "Difference", "Post link",
        "Job link",
    ],
    "More Instagram finds": [
        "Company", "Role", "Experience", "Location", "Post date",
        "Contact email", "Phone", "Website or careers link", "Account", "Notes",
    ],
    "Requirements check": [
        "Company", "Role", "Their requirement", "Your profile", "Verdict",
        "Reason",
    ],
    "Excluded": ["Company", "Role", "Reason"],
    "Notes": ["Item", "Detail"],
}
JSON_KEYS = {
    "Shortlist": "shortlist",
    "Instagram vs LinkedIn": "instagram_vs_linkedin",
    "More Instagram finds": "more_instagram_finds",
    "Requirements check": "requirements_check",
    "Excluded": "excluded",
    "Notes": "notes",
}

FONT = "Arial"
HEADER_FILL = PatternFill("solid", fgColor="1F3864")


def key_of(col: str) -> str:
    return col.lower().replace(" ", "_")


def main(src: str, dst: str) -> None:
    with open(src, encoding="utf-8") as fh:
        data = json.load(fh)

    wb = Workbook()
    wb.remove(wb.active)
    for tab, cols in TABS.items():
        ws = wb.create_sheet(tab)
        ws.append(cols)
        for cell in ws[1]:
            cell.font = Font(name=FONT, bold=True, color="FFFFFF")
            cell.fill = HEADER_FILL
            cell.alignment = Alignment(wrap_text=True, vertical="center")
        for row in data.get(JSON_KEYS[tab], []):
            values = []
            for col in cols:
                val = row.get(key_of(col), "")
                if col == "Contact email" and not val:
                    val = "Not published"
                values.append(val)
            ws.append(values)
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.font = Font(name=FONT)
                cell.alignment = Alignment(wrap_text=True, vertical="top")
        for idx, col in enumerate(cols, start=1):
            longest = max(
                [len(col)] + [len(str(c.value or "")) for c in ws[ws.cell(1, idx).column_letter]]
            )
            ws.column_dimensions[ws.cell(1, idx).column_letter].width = min(max(12, longest + 2), 50)
        ws.freeze_panes = "A2"

    wb.save(dst)
    print(f"saved {dst}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
