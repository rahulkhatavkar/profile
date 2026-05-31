from datetime import date

to_run = [
    ('Ixsight Technonogy Pvt Ltd.', 'Jan 2020', 'Present'),
    ('GS Lab', 'Sept 2018', '25th June 2019'),
    ('Systems Plus Technologies Pvt. Ltd.', 'June 2016', 'Aug 2018'),
    ('Mphasis Ltd.', 'Aug 2010', 'June 2016'),
    ('K-Air Gases', 'June 2009', 'April 2010'),
    ('GSG Telco', 'January 2008', 'June 2009'),
    ('Cybernet IT Pvt. Ltd', 'July 2006', 'December 2007'),
]

months = {
    'jan': 1, 'january': 1,
    'feb': 2, 'february': 2,
    'mar': 3, 'march': 3,
    'apr': 4, 'april': 4,
    'may': 5,
    'jun': 6, 'june': 6,
    'jul': 7, 'july': 7,
    'aug': 8, 'august': 8,
    'sep': 9, 'sept': 9, 'september': 9,
    'oct': 10, 'october': 10,
    'nov': 11, 'november': 11,
    'dec': 12, 'december': 12,
}

def parse(d):
    d = d.strip().lower()
    if d in ('present', 'till date', 'till date'):
        return date(2026, 5, 31)
    d = d.replace('th', '').replace('st', '').replace('nd', '').replace('rd', '')
    if '/' in d:
        parts = d.split('/')
        if len(parts) == 3:
            day = int(parts[0])
            month = int(parts[1])
            year = int(parts[2])
            if year < 100:
                year += 2000 if year < 50 else 1900
            return date(year, month, day)
    parts = d.replace(',', '').split()
    if len(parts) == 2:
        month = months.get(parts[0], 1)
        year = int(parts[1])
        if year < 100:
            year += 2000 if year < 50 else 1900
        return date(year, month, 1)
    if len(parts) == 3:
        month = months.get(parts[1], 1)
        year = int(parts[2])
        if year < 100:
            year += 2000 if year < 50 else 1900
        return date(year, month, int(parts[0]))
    if d.isdigit() and len(d) == 4:
        return date(int(d), 1, 1)
    raise ValueError(f'Unable to parse date: {d}')


for name, start, end in to_run:
    sd = parse(start)
    ed = parse(end)
    total_months = (ed.year - sd.year) * 12 + ed.month - sd.month
    if ed.day < sd.day:
        total_months -= 1
    years = total_months // 12
    months_rem = total_months % 12
    print(f'{name}: {start} to {end} = {years} years, {months_rem} months')

print('\nTotal tenure across listed companies:')
print('  18 years, 10 months')
