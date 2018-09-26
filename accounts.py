class Accounts:

    accounts_list = {'Rapha':'1234'}

    def create_account(self,name,password):
        if self.account_existance(name,password) == "User not exists":
            self.accounts_list[name] = password
            return "Account created"
        else:
            return "Account exists!"

    def account_existance(self,name,password):
        key, value = name, password
        if key in self.accounts_list and self.accounts_list[key] == value:
            return "User exists"
        else:
            return "User not exists"
