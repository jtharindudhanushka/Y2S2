from uml import D


def deco(comp, cops, base, bops, dec, dattr, concs, extra_note=None, client=None):
    """concs: list of (name, attrs, ops)"""
    d = D(720)
    c = d.cls(comp, 230, 5, stereo='interface', attrs=None, ops=cops)
    b = d.cls(base, 10, 120, attrs=None, ops=bops)
    dd = d.cls(dec, 330, 110, stereo='abstract', abstract=True, attrs=[dattr], ops=['+ ' + dec + '(' + dattr.split(':')[0].strip('- ').strip() + ')'] + cops)
    d.tree(c, [b, dd], 'realize')
    # aggregation: decorator has-a component
    rx = dd.x + dd.w
    d.link([(rx, dd.y + 40), (rx + 25, dd.y + 40), (rx + 25, c.cy), (c.x + c.w, c.cy)], 'agg')
    d.text(rx + 29, c.cy + 30, 'wraps 1', 9.5, italic=True)
    y = dd.y + dd.h + 40
    xs = 160
    kids = []
    for i, (n, a, o) in enumerate(concs):
        k = d.cls(n, xs, y, attrs=a, ops=o)
        kids.append(k)
        xs = k.x + k.w + 15
    d.tree(dd, kids, 'inherit')
    if client:
        cl = d.cls(client, 10, 10, attrs=None, ops=None)
        d.link([cl.right(), (c.x, cl.cy)], 'assoc', 'uses')
    if extra_note:
        d.note(10, 215, 140, extra_note)
    return d.svg()


def coffee():
    return deco('Coffee', ['+ getDescription() : String', '+ getCost() : double'],
                'Espresso', ['+ getDescription()', '+ getCost()'],
                'CoffeeDecorator', '# coffee : Coffee',
                [('MilkDecorator', None, ['+ getDescription()', '+ getCost()']),
                 ('SugarDecorator', None, ['+ getDescription()', '+ getCost()']),
                 ('ChocolateDecorator', None, ['+ getDescription()', '+ getCost()'])],
                ['Each concrete decorator', 'adds its own text and', 'price, then calls coffee.'])


def profile():
    return deco('UserProfile', ['+ getDetails() : String', '+ getFeatures() : List<String>'],
                'BasicUserProfile', ['- name, email, picture', '+ getDetails()', '+ getFeatures()'],
                'ProfileDecorator', '# profile : UserProfile',
                [('PremiumBadgeDecorator', None, ['+ getDetails()', '+ getFeatures()']),
                 ('TwoFactorAuthDecorator', ['- phone : String'], ['+ getFeatures()', '+ verify(code) : boolean']),
                 ('ProfileThemeDecorator', ['- theme : String'], ['+ getDetails()', '+ getFeatures()'])])


def kiosk():
    return deco('CheckoutItem', ['+ getCost() : double', '+ getDescription() : String'],
                'GroceryItem', ['- name : String', '- price : double', '+ getCost()', '+ getDescription()'],
                'AddOnDecorator', '# item : CheckoutItem',
                [('GiftWrap', None, ['+ getCost()']), ('EcoBag', None, ['+ getCost()']), ('ExpressPacking', None, ['+ getCost()'])])


def course():
    return deco('Course', ['+ getFeatures() : String', '+ getPrice() : double'],
                'BaseCourse', ['+ getFeatures()', '+ getPrice()'],
                'CourseDecorator', '# course : Course',
                [('AIAssistant', None, ['+ getFeatures()', '+ getPrice()']),
                 ('PremiumMaterials', None, ['+ getFeatures()', '+ getPrice()']),
                 ('MentorSupport', None, ['+ getFeatures()', '+ getPrice()'])])


U = {'coffee': coffee, 'profile': profile, 'kiosk': kiosk, 'course': course}
