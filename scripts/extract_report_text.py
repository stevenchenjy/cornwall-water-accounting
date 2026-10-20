from _common import ROOT, latest_receipts
from pypdf import PdfReader
import shutil
import subprocess
import os

def extract_pages(path):
    reader = PdfReader(path)
    poppler = os.environ.get('PDFTOTEXT') or shutil.which('pdftotext')
    if poppler:
        result = subprocess.run([poppler, '-layout', '-enc', 'UTF-8', str(path), '-'], capture_output=True, check=True)
        pages = result.stdout.decode('utf-8').split('\f')
        if pages and not pages[-1].strip():
            pages.pop()
        if len(pages) != len(reader.pages):
            raise ValueError('Text extraction page count does not match PDF; inspect original')
        return pages, 'Poppler pdftotext'
    return [(page.extract_text() or '') for page in reader.pages], 'pypdf'

def main():
    out = ROOT / 'data/interim/report-text'
    out.mkdir(parents=True, exist_ok=True)
    receipts = latest_receipts()
    missing = []
    failed = []
    for year in range(2019, 2026):
        source_id = f'awqr-{year}'
        receipt = receipts.get(source_id)
        if not receipt:
            missing.append(source_id)
            continue
        try:
            texts, backend = extract_pages(ROOT / receipt['local_path'])
            pages = [f'=== PHYSICAL PDF PAGE {i} ===\n' + text for i, text in enumerate(texts, 1)]
            (out / f'{source_id}.txt').write_text('\n\n'.join(pages), encoding='utf-8')
            print(source_id, len(texts), f'pages via {backend}; automatic text extraction only')
        except Exception as error:
            failed.append(f'{source_id}: {error}')
    if missing or failed:
        raise SystemExit('Incomplete text extraction. Missing snapshots: ' + ', '.join(missing) + '\nFailures: ' + '; '.join(failed) + '\nKeep originals and inspect visually. Poppler pdftotext is preferred for complex legacy PDFs.')

if __name__ == '__main__':
    main()
