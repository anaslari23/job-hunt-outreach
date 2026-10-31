#!/usr/bin/env python3
"""Re-open the workbook and report rows per tab and rule violations.

Usage: python3 verify_spreadsheet.py AI_Job_Outreach_Nov2026.xlsx
Exit code 1 if a problem is found.
"""
import sys

from openpyxl import load_workbook

EXPECTED = [
    "Shortlist", "Instagram vs LinkedIn", "More Instagram finds",
    "Requirements check", "Excluded", "Notes",
]


def main(path: str) -> int:
    wb = load_workbook(path)
    problems = []
    for name in EXPECTED:
        if name not in wb.sheetnames:
            problems.append(f"missing tab: {name}")
    for ws in wb.worksheets:
        rows = ws.max_row - 1
        print(f"{ws.title}: {rows} data rows, frozen={ws.freeze_panes}")
        if ws.freeze_panes != "A2":
            problems.append(f"{ws.title}: header row not frozen")
        if ws.merged_cells.ranges:
            problems.append(f"{ws.title}: merged cells present")

    if "Shortlist" in wb.sheetnames:
        ws = wb["Shortlist"]
        headers = [c.value for c in ws[1]]
        if "Contact email" in headers and "Email source" in headers:
            e_idx = headers.index("Contact email")
            s_idx = headers.index("Email source")
            for r in ws.iter_rows(min_row=2, values_only=True):
                email, source = r[e_idx], r[s_idx]
                if email and email != "Not published" and not source:
                    problems.append(f"email without source: {email}")

    for p in problems:
        print("PROBLEM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
