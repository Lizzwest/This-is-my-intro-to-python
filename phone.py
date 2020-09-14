class Phone():
    def __init__(self, phone_number):
        self.number = phone_number

    def call(self, other_number):
        print("Calling {} from {}".format(other_number, self.number))
    def text(self, other_number, msg):
        print("sending a text to {} from {}".format(other_number, self.number))
        print(msg)
    def open_app(self, app_name):
        print("Opening {} on device".format(app_name))
class Iphone(Phone):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.fingerprint = None

    def set_fingerprint(self, new_fingerprint):
        self.fingerprint = new_fingerprint
    def unlock(self, fingerprint=None):
        if(fingerprint == None and self.fingerprint== None):
            print("phone is unlocked because no fingerprint is set")
        if(fingerprint == self.fingerprint):
            print("phone unlocked")
        else:
            print("phone locked, fingerprint doesnt match")

martin_iphone = Iphone (9995556789)
print("Martins number is {}".format(martin_iphone.number))

martin_iphone.set_fingerprint("password")
print(martin_iphone.fingerprint)

martin_iphone.unlock("password123")
martin_iphone.call(1234567890)
martin_iphone.open_app("tik tok")
