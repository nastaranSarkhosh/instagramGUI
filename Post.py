class Post:
    def __init__(self,title,text):
        self.title = title
        self.text = text
        self.like=0
        self.accountLike=[]
    def likePost2(self,username):
        for usernameA in self.accountLike:
            if usernameA==username:
                return -1
        self.accountLike.append(username)
        self.like+=1
        return 1

    def dislikePost2(self, username):
        for usernameA in self.accountLike:
            if usernameA == username:
                self.like-=1
                self.accountLike.remove(username)
                return 1

        return -1