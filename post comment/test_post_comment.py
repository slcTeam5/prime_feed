import unittest

from post_comment import PostComment

class PostfeedtestCase(unittest.TestCase):
    def setUp(self):
        self.myfeed = PostComment()
    
    def test_body(self):
        self.assertEqual(self.myfeed.body,"",msg ="Article has no body")
   
    def test_postId(self):
        self.assertEqual(self.myfeed.PostId,"",msg ="Article has no PostId")

    def test_Id(self):
        self.assertEqual(self.myfeed.Id,0,msg ="has no id ")

    def test_post_feed(self):
       self.myfeed.create_feed("This is My body","postid2",3)
       self.assertEqual(self.myfeed.feed,{"body":"This is My body","postId":"postid2","id":3},msg ="A feed not has not been created")
    
        