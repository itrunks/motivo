import csv,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
base=root/'research/india'
def read(name):
    with (base/name).open(encoding='utf-8',newline='') as f:
        return list(csv.DictReader(f))
registry=read('stage2-source-registry.csv')
links=read('stage2-source-crosswalk.csv')
ids={r['source_id']:r['source_url'] for r in registry}
assert len(ids)==len(registry)==len(set(ids.values())), 'duplicate registry identity'
assert all(u.startswith('https://') for u in ids.values())
seen=set()
for r in links:
    key=(r['brand'],r['model'],r['source_url'])
    assert key not in seen, key
    seen.add(key)
    assert ids.get(r['source_id'])==r['source_url'], key
    path=(root/r['evidence_path']).resolve()
    assert path.is_relative_to(base.resolve())
    models=json.loads(path.read_text())['models']
    assert any(m['brand']==r['brand'] and m['model']==r['model'] for m in models), key
for path in {r['evidence_path'] for r in links}:
    for m in json.loads((root/path).read_text())['models']:
        assert (m['brand'],m['model'],m['source_url']) in seen, m['model']
        for u in [m.get('observations',{}).get('brochure'),m.get('observations',{}).get('price_conflict_source'),m.get('observations',{}).get('maintenance',{}).get('source_url')]:
            if u: assert (m['brand'],m['model'],u) in seen, u
print(f'PASS: {len(registry)} sources, {len(links)} mappings')
