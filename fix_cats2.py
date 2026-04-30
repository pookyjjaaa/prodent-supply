import re, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = r'C:\Catalago Prodent\website\js\products-data.js'
with open(path, encoding='utf-8') as f:
    content = f.read()

changes = 0

fixes = [
    # (id,               old_cat,       new_cat)
    ('borgatta-013',    'desechables', 'ortodoncia'),
    ('medesy-1017',     'equipos',     'desechables'),
    ('medesy-1018',     'equipos',     'desechables'),
    ('medesy-1022',     'equipos',     'materiales'),
    ('vamasa-049',      'instrumental','desechables'),
]

for pid, old_cat, new_cat in fixes:
    pattern = f"(id:'{pid}'[^}}]*?)cat:'{old_cat}'"
    new_content = re.sub(pattern,
                         lambda m, nc=new_cat: m.group(1) + f"cat:'{nc}'",
                         content, flags=re.DOTALL)
    if new_content != content:
        content = new_content
        changes += 1
        print(f"  Fixed {pid}: {old_cat} → {new_cat}")
    else:
        print(f"  SKIPPED {pid} (pattern not found)")

print(f"\nTotal cambios: {changes}")
total = len(re.findall(r"id:'[a-zA-Z0-9_-]+'", content))
print(f"Total productos: {total}")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
print("GUARDADO")
