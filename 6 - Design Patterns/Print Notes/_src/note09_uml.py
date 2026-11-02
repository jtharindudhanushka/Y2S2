from uml import D


def stuml(ctx, cattrs, cops, iface, iops, states, client='Client', note=None):
    d = D(720)
    cl = d.cls(client, 10, 25, attrs=None, ops=None)
    c = d.cls(ctx, 150, 8, stereo='Context', attrs=cattrs, ops=cops)
    i = d.cls(iface, 470, 8, stereo='interface', attrs=None, ops=iops)
    d.link([cl.right(), (c.x, cl.cy)], 'assoc', 'uses')
    d.link([(c.x + c.w, i.cy), (i.x, i.cy)], 'agg', 'currentState 1', lx=c.x + c.w + 18, ly=i.cy - 5)
    y = max(c.y + c.h, i.y + i.h) + 40
    xs, kids = 10, []
    for n, o in states:
        k = d.cls(n, xs, y, attrs=None, ops=o)
        kids.append(k); xs = k.x + k.w + 12
    d.tree(i, kids, 'realize', gap=(y - 14) - (i.y + i.h))
    # states change the context's state (dependency back to context)
    k0 = kids[0]
    d.link([(k0.cx - 20, k0.y), (k0.cx - 20, c.y + c.h + 8), (c.x + 30, c.y + c.h + 8), (c.x + 30, c.y + c.h)], 'dep')
    d.text(c.x + 36, c.y + c.h + 21, 'states call context.setState(next)', 9, italic=True)
    if note:
        d.note(10, y + 70, 300, note)
    return d.svg()


def sm(states, trans, w=720, h=150, init=None, final=None):
    """states: name -> (x,y,w); trans: list of (from,to,label, pts|None, lx, ly)"""
    d = D(w, h)
    S = {}
    for n, (x, y, ww) in states.items():
        S[n] = d.state(n, x, y, ww)
    if init:
        n, (ix, iy) = init
        d.initial(ix, iy)
        t = S[n]
        d.link([(ix + 6, iy), (t['x'], iy)], 'trans')
    if final:
        n, (fx, fy) = final
        d.final(fx, fy)
        t = S[n]
        d.link([(t['x'] + t['w'], fy), (fx - 8, fy)], 'trans')
    for f, to, label, pts, lx, ly in trans:
        d.link(pts, 'trans')
        d.text(lx, ly, label, 9, italic=True)
    return d.svg()


def tv_sm():
    st = {'OFF': (60, 50, 90), 'ON': (300, 50, 90), 'MUTE': (540, 50, 90)}
    tr = [('OFF', 'ON', 'pressOn', [(150, 60), (300, 60)], 200, 55),
          ('ON', 'MUTE', 'pressMute', [(390, 60), (540, 60)], 440, 55),
          ('ON', 'OFF', 'pressOff', [(300, 76), (150, 76)], 200, 92),
          ('MUTE', 'OFF', 'pressOff', [(585, 82), (585, 125), (105, 125), (105, 82)], 330, 120),
          ('MUTE', 'ON', 'pressOn', [(540, 76), (390, 76)], 440, 92)]
    return sm(st, tr, h=140, init=('OFF', (25, 66)))


def tv_uml():
    return stuml('TV', ['- currentState : State'], ['+ pressOnButton()', '+ pressOffButton()', '+ pressMuteButton()', '+ setState(s : State)'],
                 'State', ['+ pressOnButton(tv : TV)', '+ pressOffButton(tv : TV)', '+ pressMuteButton(tv : TV)'],
                 [('OffState', ['+ pressOnButton(tv)', '+ pressOffButton(tv)', '+ pressMuteButton(tv)']),
                  ('OnState', ['+ pressOnButton(tv)', '+ pressOffButton(tv)', '+ pressMuteButton(tv)']),
                  ('MuteState', ['+ pressOnButton(tv)', '+ pressOffButton(tv)', '+ pressMuteButton(tv)'])], 'RemoteUser')


def park_sm():
    st = {'Available': (40, 45, 100), 'Reserved': (200, 45, 100), 'Occupied': (360, 45, 100),
          'Payment Due': (520, 45, 110)}
    st2 = dict(st); st2['Closed'] = (520, 125, 110)
    tr = [('A', 'R', 'reserve()', [(140, 55), (200, 55)], 145, 50),
          ('R', 'O', 'enter()', [(300, 55), (360, 55)], 310, 50),
          ('O', 'P', 'exit()', [(460, 55), (520, 55)], 470, 50),
          ('P', 'C', 'pay()', [(575, 77), (575, 125)], 580, 105),
          ('R', 'A', 'cancel() / timeout', [(250, 77), (250, 100), (90, 100), (90, 77)], 120, 112),
          ('A', 'O', 'enter() (walk-in)', [(90, 45), (90, 25), (410, 25), (410, 45)], 220, 20),
          ('C', 'A', 'reset() - slot freed', [(520, 141), (65, 141), (65, 77)], 230, 136)]
    return sm(st2, tr, h=170, init=('Available', (15, 61)))


def park_uml():
    return stuml('ParkingSession', ['- state : ParkingState', '- vehicleNo : String', '- entryTime, exitTime', '- fee : double'],
                 ['+ reserve()', '+ enter()', '+ exit()', '+ pay(amount)', '+ setState(s)'],
                 'ParkingState', ['+ reserve(s : ParkingSession)', '+ enter(s : ParkingSession)', '+ exit(s : ParkingSession)', '+ pay(s, amount)'],
                 [('AvailableState', ['+ reserve(s)', '+ enter(s)']), ('ReservedState', ['+ enter(s)', '+ cancel(s)']),
                  ('OccupiedState', ['+ exit(s)']), ('PaymentDueState', ['+ pay(s, amt)']), ('ClosedState', ['(all: rejected)'])],
                 'ParkingApp')


def doc_sm():
    st = {'Draft': (70, 40, 95), 'Moderation': (250, 40, 110), 'Published': (450, 40, 100), 'Archived': (610, 40, 95)}
    tr = [('D', 'M', 'submit()', [(165, 50), (250, 50)], 180, 45),
          ('M', 'P', 'approve()', [(360, 50), (450, 50)], 375, 45),
          ('P', 'A', 'archive()', [(550, 56), (610, 56)], 555, 51),
          ('M', 'D', 'reject()', [(250, 66), (165, 66)], 185, 82),
          ('D', 'D', 'edit()', [(100, 40), (100, 18), (135, 18), (135, 40)], 103, 14)]
    return sm(st, tr, h=110, init=('Draft', (35, 56)), final=('Archived', (712, 90)) if False else None)


def doc_uml():
    return stuml('Document', ['- state : DocumentState', '- content : String'],
                 ['+ edit(text)', '+ submit()', '+ approve()', '+ reject()', '+ archive()', '+ setState(s)'],
                 'DocumentState', ['+ edit(d, text)', '+ submit(d)', '+ approve(d)', '+ reject(d)', '+ archive(d)'],
                 [('DraftState', ['+ edit(d,t)', '+ submit(d)']), ('ModerationState', ['+ approve(d)', '+ reject(d)']),
                  ('PublishedState', ['+ archive(d)']), ('ArchivedState', ['(all rejected)'])], 'Editor')


def kiosk_sm():
    st = {'Idle': (60, 40, 90), 'Scanning': (240, 40, 100), 'Payment': (430, 40, 100), 'Completed': (610, 40, 100)}
    tr = [('I', 'S', 'scanItem()', [(150, 50), (240, 50)], 160, 45),
          ('S', 'S', 'scanItem()', [(270, 40), (270, 18), (310, 18), (310, 40)], 275, 14),
          ('S', 'P', 'checkout()', [(340, 50), (430, 50)], 350, 45),
          ('P', 'C', 'pay() ok', [(530, 50), (610, 50)], 545, 45),
          ('P', 'S', 'cancel/fail', [(430, 66), (340, 66)], 350, 82),
          ('C', 'I', 'printReceipt() / timeout', [(660, 72), (660, 100), (105, 100), (105, 72)], 300, 96)]
    return sm(st, tr, h=110, init=('Idle', (30, 56)))


U = {'tv_sm': tv_sm, 'tv_uml': tv_uml, 'park_sm': park_sm, 'park_uml': park_uml, 'doc_sm': doc_sm,
     'doc_uml': doc_uml, 'kiosk_sm': kiosk_sm}
