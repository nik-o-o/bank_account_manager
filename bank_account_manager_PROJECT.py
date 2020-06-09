class Account:
    def __init__(self,acct_nbr,opening_deposit):
        self.acct_nbr = acct_nbr
        self.balance = opening_deposit
        
    def __str__(self):
        return f'${self.balance:.2f}'
    
    def deposit(self,dep_amt):
        self.balance += dep_amt
        
    def withdraw(self,wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
        else:
            print('Funds Unavailable')

class Checking(Account):
    def __init__(self,acct_nbr,opening_deposit):
        super().__init__(acct_nbr,opening_deposit)
    
    def __str__(self):
        return f'Checking Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'

class Savings(Account):
    def __init__(self,acct_nbr,opening_deposit):
        super().__init__(acct_nbr,opening_deposit)

    def __str__(self):
        return f'Savings Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'


class Business(Account):
    def __init__(self,acct_nbr,opening_deposit):
        super().__init__(acct_nbr,opening_deposit)

    def __str__(self):
        return f'Business Account #{self.acct_nbr}\n  Balance: {Account.__str__(self)}'

class Customer:
    def __init__(self, name, PIN):
        self.name = name
        self.PIN = PIN
        
        # dictionary of accounts, with lists to hold multiple accounts
        self.accts = {'C':[],'S':[],'B':[]}
        
    def __str__(self):
        return self.name
        
    def open_checking(self,acct_nbr,opening_deposit):
        self.accts['C'].append(Checking(acct_nbr,opening_deposit))
    
    def open_savings(self,acct_nbr,opening_deposit):
        self.accts['S'].append(Savings(acct_nbr,opening_deposit))
        
    def open_business(self,acct_nbr,opening_deposit):
        self.accts['B'].append(Business(acct_nbr,opening_deposit))

    # a method that computes a total as needed
    def get_total_deposits(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f'Combined Deposits: ${total:.2f}')
        
def make_dep(cust,acct_type,acct_num,dep_amt):
    """
    make_dep(cust, acct_type, acct_num, dep_amt)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acct_num  = integer
    dep_amt   = integer
    """
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.deposit(dep_amt)
            
def make_wd(cust,acct_type,acct_num,wd_amt):
    """
    make_dep(cust, acct_type, acct_num, wd_amt)
    cust      = variable name (Customer record/ID)
    acct_type = string 'C' 'S' or 'B'
    acct_num  = integer
    wd_amt    = integer
    """
    for acct in cust.accts[acct_type]:
        if acct.acct_nbr == acct_num:
            acct.withdraw(wd_amt)

nancy = Customer('Nancy',2)
nancy.open_business(2018,8900)
nancy.get_total_deposits()

make_wd(nancy,'B',2018,1000000)

nancy.get_total_deposits()