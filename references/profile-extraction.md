# Profile extraction (Step 1)

Build the profile from the CV text only. Every field below has a source line in the CV or a user answer. If neither exists, write "Unknown" and ask in the single questionnaire message.

## Fields

| Field | Where it comes from | Notes |
|---|---|---|
| Name, email, phone, city | CV header | Check the email and phone match what LinkedIn will pre-fill later |
| Target titles | Headline + last two roles | Three to six, ordered by fit |
| Overall experience | Dates of full-time roles | See calculation rules |
| Core-skill experience | Roles where the skill is named in the bullets | Calculated separately per skill |
| Stack | Skills section + role bullets | Keep terms as written (e.g. "LangChain", "Odoo 17") |
| Education | Education section | Include graduation year |
| Links | Header or footer | GitHub, portfolio, LinkedIn only if on the CV |
| Proof points | Strongest 2 or 3 bullets | One line each, with a number or result if the CV has one |

## Experience calculation

1. List each role with start and end month. Use "present" as the current month.
2. Count whole months per role. Round the total down to whole years and months.
3. Exclude internships, trainee periods and freelance work unless the CV presents them as full-time employment.
4. Merge overlapping roles; never count the same month twice.
5. For a core skill, add only the months of roles whose bullets name that skill.
6. Show the working to the user in the profile summary so they can correct it, for example "AI/ML Engineer, 14 months".

## Student or fresher handling

- Add intern, trainee, associate, graduate and apprentice to the title list.
- Put graduation year in every email.
- Widen the seniority band to 0 to 2 years.

## Profile summary layout (show to the user)

```
Who: <name>, <city>, <overall> overall, <core> in <core skill>
Target titles: 1) ... 2) ... 3) ...
Keywords: ...
Locations: <city>, <nearby>, remote, relocation: <yes/no/where>
Seniority band: roles asking up to <user years + 1> years
```

## Multiple CV versions

If Drive or the upload holds several versions, ask which one to use. Do not merge them. Record the filename in the Notes tab.

## Scanned PDFs

Read the pages as images. Note in the Notes tab that the text was read from images so a typo in a phone number or email is easy to trace.
