from uml import D, esc


def box(d, x, y, w, h, lines, bold0=True, fill='#fff', r=0):
    d.raw(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="#000" stroke-width="1.1"/>', y + h)
    n = len(lines)
    for i, t in enumerate(lines):
        yy = y + h / 2 + (i - (n - 1) / 2) * 12 + 4
        b = ' font-weight="bold"' if (i == 0 and bold0) else ''
        d.raw(f'<text x="{x + w / 2}" y="{yy:.1f}" font-size="10" text-anchor="middle"{b}>{esc(t)}</text>')
    return (x, y, w, h)


def decision():
    d = D(720, 330)
    Q = [('Is the problem about CREATING objects?', 10),
         ('Is it about STRUCTURE / wrapping / connecting objects?', 120),
         ('Is it about BEHAVIOUR / workflow / who handles what?', 225)]
    # creational
    box(d, 5, 10, 150, 90, ['CREATIONAL', 'object creation'], fill='#e6e6e6')
    box(d, 165, 10, 270, 40, ['Only ONE (or exactly N) instance', 'shared by everyone? -> SINGLETON (Multiton)'], bold0=False)
    box(d, 445, 10, 270, 40, ['Create one of several TYPES chosen at', 'runtime, hide "new"? -> FACTORY METHOD'], bold0=False)
    box(d, 165, 58, 550, 40, ['Signals: "only one", "single global", "same file", "unique ID"  |  "different types of X',
                              'depending on user request", "too many if-else for creation"'], bold0=False, fill='#f6f6f6')
    # structural
    box(d, 5, 112, 150, 100, ['STRUCTURAL', 'composition /', 'wrapping'], fill='#e6e6e6')
    box(d, 165, 112, 135, 48, ['Interface INCOMPATIBLE', '(legacy / vendor)', '-> ADAPTER'], bold0=False)
    box(d, 305, 112, 135, 48, ['Many subsystems,', 'want ONE simple entry', '-> FACADE'], bold0=False)
    box(d, 445, 112, 135, 48, ['SAME interface, CONTROL', 'access / lazy / cache', '-> PROXY'], bold0=False)
    box(d, 585, 112, 130, 48, ['SAME interface, ADD', 'optional features', '-> DECORATOR'], bold0=False)
    box(d, 165, 166, 550, 46, ['Signals: "cannot modify", "different method signatures"  |  "one interface for inventory, payment..."  |',
                               '"restricted / load only a few pages / permissions"  |  "add-ons without subclasses for every combination"'], bold0=False, fill='#f6f6f6')
    # behavioural
    box(d, 5, 224, 150, 100, ['BEHAVIOURAL', 'responsibility /', 'communication'], fill='#e6e6e6')
    box(d, 165, 224, 180, 48, ['SAME steps in fixed order,', 'some steps differ per type', '-> TEMPLATE METHOD'], bold0=False)
    box(d, 350, 224, 180, 48, ['Request passes LEVELS / checks', 'until one handles (or all pass)', '-> CHAIN OF RESPONSIBILITY'], bold0=False)
    box(d, 535, 224, 180, 48, ['Object moves through STATES;', 'same action behaves differently', '-> STATE'], bold0=False)
    box(d, 165, 278, 550, 46, ['Signals: "follow the same overall process", "however X is different"  |  "levels of support / approval limits /',
                               'sequence of checks, easy to extend"  |  "can be in states", "transitions to", "draw a state diagram"'], bold0=False, fill='#f6f6f6')
    return d.svg()


def ecommerce():
    d = D(720)
    cl = d.cls('OrderService', 10, 10, attrs=None, ops=['+ placeOrder(o)'])
    v = d.cls('Validator', 10, 80, stereo='CoR handler', abstract=True, attrs=['# next : Validator'], ops=['+ validate(o) : boolean'])
    vs = [d.cls(n, 5 + i * 0, 0, attrs=None, ops=None) for i, n in enumerate([])]
    k1 = d.cls('InventoryCheck', 5, 175, attrs=None, ops=None)
    k2 = d.cls('FraudCheck', 5, 205, attrs=None, ops=None)
    k3 = d.cls('DeliveryAreaCheck', 5, 235, attrs=None, ops=None)
    for k in (k1, k2, k3):
        d.link([(k.x + k.w, k.cy), (v.x + v.w + 15, k.cy), (v.x + v.w + 15, v.y + v.h - 10), (v.x + v.w, v.y + v.h - 10)], 'inherit')
    f = d.cls('PaymentFactory', 250, 10, stereo='Factory', attrs=None, ops=['_+ create(method) : PaymentProcessor'])
    p = d.cls('PaymentProcessor', 250, 95, stereo='Template', abstract=True, attrs=None,
              ops=['+ handlePayment(o) {final}', '# validate(o)', '*# processPayment(o)', '# sendReceipt(o)'])
    c1 = d.cls('CreditCardProcessor', 250, 215, attrs=None, ops=None)
    c2 = d.cls('PayPalProcessor', 420, 215, attrs=None, ops=None)
    c3 = d.cls('CODProcessor', 560, 215, attrs=None, ops=None)
    d.tree(p, [c1, c2, c3], 'inherit')
    g = d.cls('OrderIdGenerator', 520, 95, stereo='Singleton', attrs=['_- instance', '- counter : AtomicLong'],
              ops=['_+ getInstance()', '+ nextId() : String'])
    d.link([cl.bottom(), v.top()], 'assoc', '1. validate')
    d.link([(cl.x + cl.w, cl.cy), (f.x, cl.cy)], 'assoc', '2. create')
    d.link([(f.cx, f.y + f.h), (f.cx, p.y)], 'dep', 'creates')
    d.link([(p.x + p.w, p.y + 30), (g.x, p.y + 30)], 'dep', '3. nextId()')
    return d.svg()


def micro():
    d = D(720, 260)
    box(d, 5, 95, 85, 50, ['Clients', 'web / mobile'])
    box(d, 115, 85, 95, 70, ['API Gateway', 'auth (JWT/OAuth)', 'routing, rate limit'], fill='#eee')
    svcs = ['User / Profile', 'Catalog / Content', 'Order / Borrow', 'Billing / Payment', 'Notification', 'Analytics / Recs']
    for i, s in enumerate(svcs):
        y = 8 + i * 40
        box(d, 250, y, 120, 32, [s + ' Svc'])
        d.raw(f'<ellipse cx="420" cy="{y + 16}" rx="28" ry="12" fill="#fff" stroke="#000"/><text x="420" y="{y + 20}" font-size="9" text-anchor="middle">own DB</text>')
        d.link([(370, y + 16), (392, y + 16)], 'line')
        d.link([(210, 120), (232, 120), (232, y + 16), (250, y + 16)], 'assoc')
    box(d, 480, 30, 110, 60, ['Message broker', 'Kafka / RabbitMQ', 'events, sagas'], fill='#eee')
    box(d, 480, 110, 110, 50, ['Service registry', '+ config server'])
    box(d, 480, 175, 110, 60, ['Monitoring', 'logs, metrics,', 'tracing, alerts'])
    box(d, 605, 30, 110, 60, ['Docker + Kubernetes', 'auto-scaling,', 'self-healing'], fill='#eee')
    box(d, 605, 110, 110, 50, ['CI/CD pipeline', 'per service'])
    box(d, 605, 175, 110, 60, ['CDN / cache', 'Redis, edge', 'servers'])
    d.link([(90, 120), (115, 120)], 'assoc')
    d.text(250, 255, 'Each service: own codebase, own DB, own deployment; talk via REST/gRPC (sync) or events (async)', 9, italic=True)
    return d.svg()


U = {'decision': decision, 'ecommerce': ecommerce, 'micro': micro}
