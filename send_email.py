import yagmail

try:
    for x in range(1):
        yagmail.register('felefwlab', 'franklinelectric')
        yag = yagmail.SMTP('felefwlab')
        to = 'amjadmasood2007@gmail.com'
        subject = 'This is obviously the subject'
        body = 'This is obviously the body'
        html = '<a href="https://pypi.python.org/pypi/sky/">Click me!</a>'
        img = './test_image.png'
        yag.send(to = to, subject = subject, contents = [body, html, img])
        print("email sent successfully...")
except:
    print("something bad happened...")