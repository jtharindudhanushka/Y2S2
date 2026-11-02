from uml import D


def proxy(subject='Subject', sops=('+ request() : void',), real='RealSubject', px='Proxy',
          pattrs=('- realSubject : RealSubject',), pops=('+ request() : void',), rattrs=None, client='Client', note=None):
    d = D(700)
    s = d.cls(subject, 250, 10, stereo='interface', attrs=None, ops=list(sops))
    c = d.cls(client, 10, 20, attrs=None, ops=None)
    p = d.cls(px, 120, 120, attrs=list(pattrs), ops=list(pops))
    r = d.cls(real, 460, 120, attrs=rattrs, ops=list(sops))
    d.link([c.right(), (s.x, c.cy)], 'assoc', 'uses', lx=c.x + c.w + 8, ly=c.cy - 4)
    d.tree(s, [p, r], 'realize')
    d.link([(p.x + p.w, p.cy + 10), (r.x, p.cy + 10)], 'assoc', 'has-a / delegates', lx=p.x + p.w + 10, ly=p.cy + 4)
    if note:
        d.note(10, 200 if p.y + p.h < 200 else p.y + p.h + 10, 330, note)
    return d.svg()


def generic():
    return proxy(note=['Proxy and RealSubject implement the same interface;',
                       'Proxy checks / logs / caches / lazy-loads, then forwards.'])


def image():
    return proxy('Image', ['+ display() : void'], 'RealImage', 'ProxyImage',
                 ['- fileName : String', '- realImage : RealImage'], ['+ display() : void'],
                 ['- fileName : String'], 'ImageViewer')


def document():
    return proxy('Document', ['+ getPage(n : int) : Page'], 'LargeDocument', 'DocumentProxy',
                 ['- path : String', '- cache : Map<Integer,Page>', '- doc : LargeDocument'], ['+ getPage(n : int) : Page'],
                 ['- pages : List<Page>'], 'LMSReader')


def rare():
    return proxy('BookArchive', ['+ getBook(id) : RareBook'], 'RestrictedArchive', 'ArchiveAccessProxy',
                 ['- archive : RestrictedArchive', '- user : User'], ['+ getBook(id) : RareBook', '- hasPermission() : boolean'],
                 None, 'LibraryUser')


U = {'generic': generic, 'image': image, 'document': document, 'rare': rare}
