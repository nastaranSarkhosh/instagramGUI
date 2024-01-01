import Post


class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.follower=0
        self.followerAccount=[]
        self.followingAccount=[]
        self.posts = []
        self.following=0
        self.numPost=0
        self.bio=''
        self.recentSearch=[]
        self.numRecentSearch=0
        self.suggestAccount=[]
    def findFollowing(self,username):
        for usernamef in self.followingAccount:
            if usernamef == username:
                return 1
        return -1
    def newPost(self,title,text):
        new=Post.Post(title=title,text=text)
        self.numPost+=1
        self.posts.append(new)
        return new
    def getLastPost(self):
        return self.posts[self.numPost-1]
    def deletePost(self, title,text):
        for post in self.posts:
            if post.title == title:
                if post.text==text:
                    self.posts.remove(post)
                    self.numPost-=1
    def editPost(self, title,text,newTitle,newText):
        for post in self.posts:
            if post.title == title:
                if post.text==text:
                    post.text=newText
                    post.title=newTitle

    def getRecentSearch(self,index):
        return self.recentSearch[index]
    def addFollower(self,username):
        self.follower+=1
        self.followerAccount.append(username)
    def addFollowing(self,username):
        self.following+=1
        self.followingAccount.append(username)
    def remoweFollowing(self,username):
        self.following-=1
        self.followingAccount.remove(username)
    def remoweFollower(self,username):
        self.follower-=1
        self.followerAccount.remove(username)
    def likePost(self, title,text,username):
        for post in self.posts:
            if post.title == title:
                if post.text==text:
                      return post.likePost2(username)

    def dislikePost(self, title, text, username):
        for post in self.posts:
            if post.title == title:
                if post.text == text:
                    return post.dislikePost2(username)
    def addRecentAccount(self,username):
        for usernameA in self.recentSearch:
            if username==usernameA:
                return 1
        if self.numRecentSearch<4:
           self.recentSearch.append(username)
           self.numRecentSearch+=1
        else:
            self.recentSearch.remove(self.recentSearch[0])
            self.recentSearch.append(username)


