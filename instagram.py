import Account
class Instageram:
    numAccount=1
    acounts=[Account.Account("nastaran","1")]
    @classmethod
    def creatAccount(cls,username,password):
        new=Account.Account(username,password)
        cls.acounts.append(new)
        cls.numAccount+=1
        return new

    @classmethod
    def findAccount(cls, username):
        for account in cls.acounts:
            if account.username == username:
                return cls.acounts.index(account)
        return -1
    @classmethod
    def sameFollowing(cls,username1,username2):
        same=0
        index2 = cls.findAccount(username2)
        index=cls.findAccount(username1)
        account=cls.acounts[index]
        account2=cls.acounts[index2]
        for accountFollowing in account.followingAccount:
            if account2.findFollowing(accountFollowing)==1:
                same+=1
        same1=account.following-same
        same2=account2.following-same
        sum=same1+same2
        if sum==0:
            return 0
        result=same/sum

        return result
