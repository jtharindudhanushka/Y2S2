from uml import D


def cor(handler, hattrs, hops, concs, req=None, client='Client', note=None):
    d = D(720)
    c = d.cls(client, 10, 25, attrs=None, ops=None)
    h = d.cls(handler, 230, 8, stereo='abstract', abstract=True, attrs=hattrs, ops=hops)
    rx = h.x + h.w
    d.link([(rx, h.y + 30), (rx + 30, h.y + 30), (rx + 30, h.y + h.h - 12), (rx, h.y + h.h - 12)], 'assoc')
    d.text(rx + 34, h.y + 50, 'next 0..1', 9.5, italic=True)
    d.link([c.right(), (h.x, c.cy)], 'assoc', 'sends to first')
    if req:
        r = d.cls(req[0], 10, 90, attrs=req[1], ops=req[2])
        d.link([(h.x, h.y + h.h - 10), (r.x + r.w, h.y + h.h - 10)], 'dep', 'handles', lx=r.x + r.w + 4, ly=h.y + h.h - 14)
    y = max(h.y + h.h, d.maxy) + 40
    xs, kids = 10, []
    for n, at, o in concs:
        k = d.cls(n, xs, y, attrs=at, ops=o)
        kids.append(k); xs = k.x + k.w + 14
    d.tree(h, kids, 'inherit', gap=(y - 14) - (h.y + h.h))
    if note:
        d.note(rx + 110, 10, 190, note)
    return d.svg()


def generic():
    return cor('Handler', ['# next : Handler'], ['+ setNext(h : Handler) : Handler', '*+ handleRequest(r : Request) : void'],
               [('ConcreteHandler1', None, ['+ handleRequest(r)']), ('ConcreteHandler2', None, ['+ handleRequest(r)']),
                ('ConcreteHandler3', None, ['+ handleRequest(r)'])],
               note=['if (canHandle(r)) handle it;', 'else if (next != null)', '    next.handleRequest(r);'])


def support():
    return cor('SupportHandler', ['# next : SupportHandler'],
               ['+ setNext(h) : SupportHandler', '+ handle(r) : void  {final}', '- logRequest(r)', '*# attemptToSolve(r) : boolean', '- logResolution(r)'],
               [('L1Support', None, ['# attemptToSolve(r)']), ('L2Support', None, ['# attemptToSolve(r)']),
                ('L3Support', None, ['# attemptToSolve(r)']), ('SpecialistSupport', None, ['# attemptToSolve(r)'])],
               req=('SupportRequest', ['- type : IssueType', '- description : String'], None), client='SupportDesk')


def spam():
    return cor('SpamFilter', ['# next : SpamFilter'], ['+ setNext(f) : SpamFilter', '*+ check(e : Email) : Verdict'],
               [('SenderFilter', None, ['+ check(e)']), ('TimeFilter', None, ['+ check(e)']),
                ('ContentFilter', None, ['+ check(e)']), ('AttachmentFilter', None, ['+ check(e)'])],
               req=('Email', ['- sender, sentTime', '- body, attachments'], None), client='MailServer')


def validation():
    return cor('Validator', ['# next : Validator'], ['+ linkWith(v) : Validator', '*+ validate(o) : boolean'],
               [('InventoryCheck', None, ['+ validate(o)']), ('FraudCheck', None, ['+ validate(o)']),
                ('DeliveryAreaCheck', None, ['+ validate(o)'])], client='OrderService')


U = {'generic': generic, 'support': support, 'spam': spam, 'validation': validation}
