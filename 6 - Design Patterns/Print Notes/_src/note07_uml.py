from uml import D


def tm(abs_name, attrs, ops, concs, note=None, client=None):
    d = D(720)
    a = d.cls(abs_name, 200, 8, stereo='abstract', abstract=True, attrs=attrs, ops=ops)
    y = a.y + a.h + 40
    xs, kids = 20, []
    for n, at, o in concs:
        k = d.cls(n, xs, y, attrs=at, ops=o)
        kids.append(k); xs = k.x + k.w + 18
    d.tree(a, kids, 'inherit')
    if note:
        d.note(a.x + a.w + 20, 15, 205, note)
    if client:
        c = d.cls(client, 10, 20, attrs=None, ops=None)
        d.link([c.right(), (a.x, c.cy)], 'assoc', 'uses')
    return d.svg()


NOTE = ['final template method = fixed order', 'italic # = abstract primitive step',
        'plain = common (invariant) step', 'hook = optional override (default)']


def generic():
    return tm('AbstractClass', None,
              ['+ templateMethod() : void  {final}', '# commonOperation() : void', '*# primitiveOperation1() : void',
               '*# primitiveOperation2() : void', '# hook() : boolean'],
              [('ConcreteClassA', None, ['# primitiveOperation1()', '# primitiveOperation2()']),
               ('ConcreteClassB', None, ['# primitiveOperation1()', '# primitiveOperation2()', '# hook()'])], NOTE)


def course():
    return tm('OnlineCourse', ['# studentId : String', '# courseId : String'],
              ['+ completeCourse() : void  {final}', '- validateRegistration() : boolean', '*# deliverFinalAssessment() : void',
               '*# evaluatePerformance() : double', '- generateCertificate(score) : void'],
              [('ProgrammingCourse', None, ['# deliverFinalAssessment()', '# evaluatePerformance() : double']),
               ('DesignCourse', None, ['# deliverFinalAssessment()', '# evaluatePerformance() : double'])],
              ['completeCourse():', '1 validateRegistration()  common', '2 deliverFinalAssessment() varies',
               '3 evaluatePerformance()   varies', '4 generateCertificate()   common'])


def payment():
    return tm('PaymentProcessor', None,
              ['+ handlePayment(order) : void  {final}', '# validate(order) : boolean', '*# processPayment(order) : void',
               '# sendReceipt(order) : void'],
              [('CreditCardPaymentProcessor', None, ['# processPayment(order)']),
               ('PayPalPaymentProcessor', None, ['# processPayment(order)']),
               ('CashOnDeliveryProcessor', None, ['# processPayment(order)', '# sendReceipt(order)'])])


def salary():
    return tm('SalaryCalculator', ['# basic : double', '# otHours, absentDays, noPayDays'],
              ['+ calculateNetSalary() : double  {final}', '# overtime() : double', '# attendanceAllowance() : double',
               '# noPay() : double', '- gross() / epf() / tax()'],
              [('PermanentSalary', None, ['(uses defaults)']),
               ('ExecutiveSalary', None, ['# overtime() : 0', '# noPay() : 0', '# allowances()']),
               ('DailyWorkerSalary', None, ['# overtime()', '# attendanceAllowance()'])])


def checkout():
    return tm('CheckoutProcess', None,
              ['+ checkout(order) : void  {final}', '# validateCart(order) : void', '*# processPayment(order) : void',
               '*# arrangeDelivery(order) : void', '# sendConfirmation(order) : void'],
              [('DomesticCardCheckout', None, ['# processPayment()', '# arrangeDelivery()']),
               ('InternationalPayPalCheckout', None, ['# processPayment()', '# arrangeDelivery()'])])


U = {'generic': generic, 'course': course, 'payment': payment, 'salary': salary, 'checkout': checkout}
