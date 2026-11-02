from uml import D


def singleton():
    d = D(700)
    s = d.cls('PrinterManager', 250, 10, stereo='Singleton',
              attrs=['_- instance : PrinterManager', '- jobQueue : Queue<Job>'],
              ops=['- PrinterManager()', '_+ getInstance() : PrinterManager', '+ submitJob(job : Job) : void', '+ getStatus() : String'])
    a = d.cls('LabModule', 20, 20, attrs=None, ops=None)
    b = d.cls('LibraryModule', 20, 95, attrs=None, ops=None)
    d.link([a.right(), (s.x, a.cy)], 'dep', 'use')
    d.link([b.right(), (s.x, b.cy)], 'dep', 'use')
    r = s.x + s.w
    d.link([(r, s.y + 40), (r + 45, s.y + 40), (r + 45, s.y + 95), (r, s.y + 95)], 'assoc')
    d.text(r + 50, s.y + 64, 'instance', 9.5, italic=True)
    d.text(r + 50, s.y + 77, '1', 9.5)
    d.note(470, 120, 225, ['final class: no subclass can call the', 'private constructor. Underlined = static.'])
    return d.svg()


def multiton():
    d = D(360)
    d.cls('PrinterManager', 10, 8,
          attrs=['_- printers : List<PrinterManager>', '_- MAX_PRINTERS : int = 3', '_- nextPrinter : int = 0'],
          ops=['- PrinterManager()', '_+ getPrinter() : PrinterManager'])
    return d.svg()


def cricket():
    d = D(440)
    d.cls('Captain', 8, 8, stereo='Singleton', attrs=['_- instance : Captain'], ops=['- Captain()', '_+ getInstance() : Captain'])
    d.cls('Player', 190, 8, stereo='Multiton',
          attrs=['_- team : Map<Role,List<Player>>', '_- LIMIT : Map<Role,Integer>', '- name : String', '- role : Role'],
          ops=['- Player(role, name)', '_+ addPlayer(role,name) : Player'])
    return d.svg()


U = {'singleton': singleton, 'multiton': multiton, 'cricket': cricket}
