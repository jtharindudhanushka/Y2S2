from uml import D


def generic(target='Target', tops='+ request() : void', adapter='Adapter', adaptee='Adaptee',
            aops='+ specificRequest() : void', client='Client', field='- adaptee : Adaptee', w=700):
    d = D(w)
    c = d.cls(client, 10, 25, attrs=None, ops=None)
    t = d.cls(target, 250, 10, stereo='interface', attrs=None, ops=[tops])
    a = d.cls(adapter, 250, 110, attrs=[field], ops=[tops])
    e = d.cls(adaptee, 540, 110, attrs=None, ops=[aops])
    d.link([c.right(), (t.x, c.cy)], 'assoc', 'uses')
    d.link([a.top(), (a.cx, t.y + t.h)], 'realize')
    d.link([(a.x + a.w, a.cy), (e.x, a.cy)], 'comp', 'has-a / wraps', lx=a.x + a.w + 20, ly=a.cy - 5)
    return d.svg()


def printer():
    return generic('Printer', '+ print(text : String) : void', 'PrinterAdapter', 'ModernPrinter',
                   '+ printPDF(file : String) : void', 'Application', '- printer : ModernPrinter')


def scanner():
    return generic('BarcodeScanner', '+ scanBook() : String', 'ScannerAdapter', 'NewBarcodeScanner',
                   '+ readBarcode() : String', 'LibrarySystem', '- scanner : NewBarcodeScanner')


def parking():
    return generic('PaymentProcessor', '+ pay(amount : double) : boolean', 'LegacyPaymentAdapter',
                   'LegacyPaymentMachine', '+ makeTransaction(cents : int) : int', 'ParkingSession',
                   '- machine : LegacyPaymentMachine')


def multi():
    d = D(720)
    t = d.cls('HotelProvider', 250, 5, stereo='interface', attrs=None,
              ops=['+ search(city, dates) : List<Room>', '+ book(roomId) : Booking'])
    s = d.cls('HotelService', 10, 20, attrs=['- providers : List<HotelProvider>'], ops=None)
    a1 = d.cls('HiltonAdapter', 120, 120, attrs=None, ops=None)
    a2 = d.cls('ShangriLaAdapter', 280, 120, attrs=None, ops=None)
    a3 = d.cls('BookingComAdapter', 460, 120, attrs=None, ops=None)
    es = []
    for a, n, o in ((a1, 'HiltonSoapAPI', '+ findRooms(xml)'), (a2, 'ShangriLaREST', '+ getAvail(json)'), (a3, 'BookingComSDK', '+ query(req)')):
        e = d.cls(n, 0, 195, attrs=None, ops=[o]); e.x = a.cx - e.w / 2; es.append(e)
    e1, e2, e3 = es
    d.link([(s.x + s.w, s.cy), (t.x, s.cy)], 'assoc', '1..*')
    d.tree(t, [a1, a2, a3], 'realize')
    for a, e in ((a1, e1), (a2, e2), (a3, e3)):
        d.link([a.bottom(), e.top()], 'comp')
    return d.svg()


U = {'generic': generic, 'printer': printer, 'scanner': scanner, 'parking': parking, 'multi': multi}
