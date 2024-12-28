class bank_v1:
    bank_name='SBI'
    bank_ifsc=12345
    bank_branch='bangalore'
    def __init__(self):
        self.cname=input('enter your name : ')
        self.cage=int(input('enter your age :'))
        self.cbalance=int(input('enter your balance :'))
        self.caccount=int(input('enter your account no :'))

    @classmethod
    def display_bank_detail(cls):
        print(f'name of the bank is {cls.bank_name}')
        print(f'ifsc of the bank is {cls.bank_ifsc}')
        print(f'branch of the bank is {cls.bank_branch}')

    def custmer_details(self):
        print(f'custemer name : {self.cname}')
        print(f'custemer age : {self.cage}')
        print(f'custemer balance : {self.cbalance}')
        print(f'custemer account no : {self.caccount}')

    @staticmethod
    def get_intm_value():
        return int(input('enter a amount :'))
    
    def withdraw(self):
        amt=self.get_intm_value()
        if self.cbalance>=amt:
            self.cbalance-=amt
            print(f'withdraw is sucessfully completed')
            print(f'your balance is {self.cbalance}')
        else:
            print('insufficient balance...')

    def deposite(self):
        amt=self.get_intm_value()
        if 0<amt:
            self.cbalance+=amt
            print(f'deposite is sucessfully completed')
            print(f'your total balance is {self.cbalance}')
        else: 
            print('enter validate amount...')
    

class bank_v2(bank_v1):
    bank_branch = 'hyderabad'
    bank_roi = 7

    def __init__(self):
        super().__init__()
        # bank_v1.__init__(self)
        self.cpin= int(input('enter your pin :'))

    @classmethod
    def display_bank_detail(cls):
        super().display_bank_detail()
        # bank_v1.display_bank_detail()
        print(f'rate of interest of the bank is {cls.bank_roi}')

    def withdraw(self):
        epin = int(input('enter your pin : '))
        if epin == self.cpin:
            super().withdraw()
        else:
            print('Invalid PIN')


user = bank_v2()

user.display_bank_detail()
print()

user.custmer_details()
print()

user.withdraw()
print()

user.deposite()



