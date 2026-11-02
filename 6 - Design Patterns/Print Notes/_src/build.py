"""Build print notes: python build.py note01 [note02 ...]   (no args = all)

noteXX.src.html  -> {{uml:key}} replaced from noteXX_uml.py (dict U of key -> html)
                 -> noteXX.out.html -> "../<title>.pdf" via Edge headless.
"""
import glob, importlib, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
EDGE = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


def build(n):
    src = open(os.path.join(HERE, n + '.src.html'), encoding='utf-8').read()
    U = {}
    if os.path.exists(os.path.join(HERE, n + '_uml.py')):
        U = importlib.import_module(n + '_uml').U
    out = re.sub(r'\{\{uml:(\w+)\}\}', lambda m: U[m.group(1)](), src)
    title = re.search(r'<title>(.*?)</title>', out).group(1)
    op = os.path.join(HERE, n + '.out.html')
    open(op, 'w', encoding='utf-8').write(out)
    pdf = os.path.join(os.path.dirname(HERE), title + '.pdf')
    if os.path.exists(pdf): os.remove(pdf)
    url = 'file:///' + op.replace('\\', '/').replace(' ', '%20')
    subprocess.run([EDGE, '--headless=new', '--disable-gpu', '--no-first-run',
                    '--user-data-dir=' + os.path.join(os.environ['TEMP'], 'edge_pdf_profile'),
                    '--no-pdf-header-footer', '--print-to-pdf=' + pdf, url],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    import fitz
    print(f'{n}: {len(fitz.open(pdf))} pages -> {os.path.basename(pdf)}')
    return pdf


if __name__ == '__main__':
    names = sys.argv[1:] or sorted(os.path.basename(p)[:-9] for p in glob.glob(os.path.join(HERE, 'note*.src.html')))
    for n in names:
        build(n)
