class PostComment(object):
    #Initialization parameters in constrictor with a feed which is a dictionary of a comment
    #dictionary contains body,PostId and id of the comment for title and a value of string for body

     def __init__(self,body="",postId="",id=0):
         self.postId =postId
         self.body = body
         self.id=id
         
     comment={}
     def create_comment(self,body,PostId,id):
         comment.update{
             "body":body
             "postId":PostId
              "id":id
             }
         return comment
        
     
    # return comment should be completed in the intergration to post comment to API