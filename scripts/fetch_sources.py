import csv
from _common import ROOT, download, save_raw

def main():
    failures = []
    with (ROOT / 'research/source-register.csv').open(newline='', encoding='utf-8') as stream:
        sources = list(csv.DictReader(stream))
    for source in sources:
        try:
            data, resolved, content_type = download(source['url'])
            if source['format'] == 'pdf' and not data.lstrip().startswith(b'%PDF'):
                raise ValueError('Expected a PDF; received a different document')
            receipt = save_raw(source['source_id'], source['url'], data, resolved, content_type, source['format'])
            print(source['source_id'], receipt['bytes'], receipt['sha256'][:12])
        except Exception as error:
            failures.append(f"{source['source_id']}: {error}")
    if failures:
        raise SystemExit('Some sources failed; existing snapshots retained:\n' + '\n'.join(failures))

if __name__ == '__main__':
    main()
