
# Class reperesenting a User
class User:
    
    #constructor
    def __init__(self,username):
        self.username = username
        self.friends = []
        self.posts = []
    
    #adding friends
    def add_friend(self,friend):
        self.friends.append(friend)
        friend.friends.append(self)
    
    #creating posts
    def create_post(self,content):
        post = Post(content,self)
        self.posts.append(post)
    
    #likes on the post 
    def like_post(self,post):
        post.add_like(self)
    
    #comment on the post 
    def comment_on_post(self,post,comment):
        post.add_comment(comment,self)


# Class reperesenting a Post
class Post:
    
    #constructor
    def __init__(self,content,author):
        self.content = content
        self.author = author
        self.likes = []
        self.comments = []
    
    #likes
    def add_like(self,user):
        self.likes.append(user)
    
    #comments
    def add_comment(self,comment,user):
        self.comments.append((comment,user))

# Main Program
if __name__=="__main__":
    
    #creating user isinstances
    user1 = User("Arjun")
    user2 = User("Bunny")
    user3 = User("Charlie")
    
    
    #add friends
    user1.add_friend(user2)
    user2.add_friend(user3)
    user1.add_friend(user3)
    
    #User1 created the Post
    user1.create_post("Hello Everyone I am enjoying my new Social Media app")
    
    #User2 liked it
    user2.like_post(user1.posts[0])
    
    #User3 comment on the  user 1 posts
    user3.comment_on_post(user1.posts[0],"Nice to Hear that")
    user2.comment_on_post(user1.posts[0],"Wow!!")
    
    #Printing the details
    post = user1.posts[0]
    
    
    print("Post Content:", post.content)
    print("Author:", post.author.username)
    print("Likes:", len(post.likes))
    print("Comments:")
    for comment,user in post.comments:
        print(f"{user.username}: {comment}")
    
    
'''
Output:

Post Content: Hello Everyone I am enjoying my new Social Media app
Author: Arjun
Likes: 1
Comments:
Charlie: Nice to Hear that
Bunny: Wow!!


'''
    
    
    
