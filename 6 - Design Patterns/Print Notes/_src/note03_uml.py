from uml import D


def generic():
    d = D(700)
    c = d.cls('Client', 30, 30, attrs=None, ops=None)
    f = d.cls('Facade', 230, 10, attrs=['- a : SubsystemA', '- b : SubsystemB', '- c : SubsystemC'], ops=['+ simpleOperation() : void'])
    a = d.cls('SubsystemA', 520, 5, attrs=None, ops=['+ operationA()'])
    b = d.cls('SubsystemB', 520, 60, attrs=None, ops=['+ operationB()'])
    cc = d.cls('SubsystemC', 520, 115, attrs=None, ops=['+ operationC()'])
    d.link([c.right(), (f.x, c.cy)], 'assoc', 'uses only')
    for s in (a, b, cc):
        d.link([(f.x + f.w, f.cy), (s.x, s.cy)], 'assoc')
    d.text(470, 175, 'delegates; subsystems do not know the facade', 9, italic=True)
    return d.svg()


def bank():
    d = D(720)
    cu = d.cls('Customer', 10, 40, attrs=None, ops=['+ main()'])
    f = d.cls('BankService', 150, 10, stereo='Facade',
              attrs=['- accounts : Map<String,IAccount>'],
              ops=['+ createAccount(no, type)', '+ deposit(no, amt)', '+ withdraw(no, amt)', '+ transferMoney(from, to, amt)', '+ getBalance(no) : double'])
    ia = d.cls('IAccount', 470, 10, stereo='interface', attrs=None,
               ops=['+ deposit(amt) : void', '+ withdraw(amt) : void', '+ getBalance() : double'])
    s = d.cls('SavingAccount', 360, 150, attrs=['- balance : double'], ops=None)
    cr = d.cls('CurrentAccount', 500, 150, attrs=['- overdraft : double'], ops=None)
    iv = d.cls('InvestmentAccount', 650, 150, attrs=['- rate : double'], ops=None)
    d.link([cu.right(), (f.x, cu.cy)], 'assoc', 'uses', lx=cu.x + cu.w + 8, ly=cu.cy + 14)
    d.link([(f.x + f.w, ia.cy), (ia.x, ia.cy)], 'comp', 'holds 1..*', lx=f.x + f.w + 18, ly=ia.cy - 5)
    d.tree(ia, [s, cr, iv], 'realize')
    d.text(150, f.y + f.h + 18, 'Client never touches the account classes', 9, italic=True)
    return d.svg()


def travel():
    d = D(720)
    u = d.cls('TravelApp (Client)', 5, 50, attrs=None, ops=None)
    f = d.cls('TravelBookingFacade', 175, 20, stereo='Facade',
              attrs=['- air : AirTicketService', '- hotel : HotelService', '- taxi : TaxiService'],
              ops=['+ bookTrip(req) : Itinerary'])
    a = d.cls('AirTicketService', 475, 5, attrs=None, ops=['+ book(req)'])
    h = d.cls('HotelService', 475, 60, attrs=None, ops=['+ book(req)'])
    t = d.cls('TaxiService', 475, 115, attrs=None, ops=['+ book(req)'])
    d.link([u.right(), (f.x, u.cy)], 'assoc')
    for s in (a, h, t):
        d.link([(f.x + f.w, f.cy), (s.x, s.cy)], 'assoc')
    d.text(475, 180, 'each service uses Adapters to the third-party', 9, italic=True)
    d.text(475, 192, 'airline / hotel / taxi web services (Note 04)', 9, italic=True)
    return d.svg()


U = {'generic': generic, 'bank': bank, 'travel': travel}
