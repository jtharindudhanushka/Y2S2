from uml import D


def generic():
    d = D(700)
    p = d.cls('Product', 30, 10, stereo='interface', attrs=None, ops=['+ operation() : void'])
    c = d.cls('Creator', 400, 10, stereo='abstract', abstract=True, attrs=None,
              ops=['*+ factoryMethod() : Product', '+ someOperation() : void'])
    pa = d.cls('ConcreteProductA', 10, 120, attrs=None, ops=['+ operation() : void'])
    pb = d.cls('ConcreteProductB', 190, 120, attrs=None, ops=['+ operation() : void'])
    ca = d.cls('ConcreteCreatorA', 370, 120, attrs=None, ops=['+ factoryMethod() : Product'])
    cb = d.cls('ConcreteCreatorB', 580, 120, attrs=None, ops=['+ factoryMethod() : Product'])
    d.tree(p, [pa, pb], 'realize')
    d.tree(c, [ca, cb], 'inherit')
    d.link([c.left(), p.right()], 'dep', 'creates')
    d.link([ca.left(-8), (pb.x + pb.w, pb.cy - 8)], 'dep', 'new', lx=345, ly=150)
    return d.svg()


def db():
    d = D(700)
    i = d.cls('Database', 40, 10, stereo='interface', attrs=None,
              ops=['+ connect() : void', '+ create(p : Product) : void'])
    f = d.cls('DatabaseFactory', 420, 10, attrs=None,
              ops=['_+ getDatabase(type : String) : Database'])
    cl = d.cls('ProductService', 440, 110, attrs=['- db : Database'], ops=['+ save(p : Product) : void'])
    a = d.cls('MySQLDatabase', 5, 130, attrs=None, ops=['+ connect()', '+ create(p)'])
    b = d.cls('PostgreSQLDatabase', 140, 130, attrs=None, ops=['+ connect()', '+ create(p)'])
    c = d.cls('MongoDatabase', 305, 130, attrs=None, ops=['+ connect()', '+ create(p)'])
    d.tree(i, [a, b, c], 'realize')
    d.link([f.left(), (i.x + i.w, f.cy)], 'dep', 'creates')
    d.link([cl.top(), (cl.cx, f.y + f.h)], 'dep', 'asks', lx=cl.cx + 5, ly=f.y + f.h + 22)
    d.note(470, 205, 200, ['ProductService holds a Database', 'reference: knows only the interface'])
    return d.svg()


def book():
    d = D(560)
    i = d.cls('Book', 20, 10, stereo='interface', attrs=None, ops=['+ getTitle() : String', '+ getCategory() : String'])
    f = d.cls('BookFactory', 330, 20, attrs=None, ops=['_+ createBook(type, title) : Book'])
    a = d.cls('FictionBook', 5, 110, attrs=['- title : String'], ops=None)
    b = d.cls('ResearchBook', 150, 110, attrs=['- title : String'], ops=None)
    c = d.cls('Magazine', 300, 110, attrs=['- title : String'], ops=None)
    d.tree(i, [a, b, c], 'realize')
    d.link([f.left(), (i.x + i.w, f.cy)], 'dep', 'creates')
    return d.svg()


U = {'generic': generic, 'db': db, 'book': book}
