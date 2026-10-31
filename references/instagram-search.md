# Instagram search playbook (Step 2)

Goal: collect real, recent openings with a company name. Breadth first, then depth on the promising posts.

## Minimums before calling the source thin

- At least 8 distinct hashtags or keywords
- At least 3 aggregator or company accounts
- Both city words and seniority words varied

## Hashtag sets (adapt to the CV field)

AI / ML:
#aiengineerjobs #aijobsindia #hiringaiengineer #mljobs #genaijobs #llmengineer #aiintern #datasciencejobs

Software / backend:
#pythonjobs #backenddeveloperjobs #softwareengineerjobs #fullstackjobs #hiringdevelopers

ERP / Odoo:
#odoojobs #erpjobs #odoodeveloper #erpconsultant

City and level modifiers (combine with the above in the search box):
Kolkata, Bangalore, Pune, Hyderabad, Remote, WFH, Fresher, Junior, 0-2 years, Internship

## Per-post routine

1. Open the post from the grid.
2. Read the caption with the page-text tool.
3. Zoom the image. Emails, phone numbers and experience ranges are often only in the graphic.
4. Open carousels to the last slide. Apply details are often there.
5. Record: company, role, experience asked, location, post date, contact email, apply link, post URL, account name.
6. Check the post date. Older than 60 days is stale: record it, flag it, do not shortlist on that alone.

## Do not

- Like, follow, comment or DM
- Follow "comment X to get the link" funnels
- Click shortened links that hide the destination; use LinkedIn or the company site instead
- Enter credentials if Instagram shows a login wall; stop and ask the user

## Recording fields

Keep one JSON object per post. These feed `scripts/build_spreadsheet.py`:

```json
{
  "company": "",
  "role": "",
  "experience": "",
  "location": "",
  "post_date": "YYYY-MM-DD",
  "contact_email": "Not published",
  "phone": "",
  "apply_link": "",
  "post_url": "",
  "account": "",
  "stale": false,
  "notes": ""
}
```

## Posts with no company name

Record them under More Instagram finds with "No company named". They cannot be verified, so they go to Excluded as "not verifiable" and never into the shortlist.
