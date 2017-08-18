""" docopt_app.py

    Usage:
        docopt_app.py -h
        docopt_app.py primfeed view_feed
        docopt_app.py primfeed post <title> <body>
        docopt_app.py primfeed comment <postId> <title> <body>
        docopt_app.py <required> [-f | -g | -o ]
        docopt_app.py <repeating>...
    Options:
        -h,--help       : show this help message
        body
        postId
        primfeed view_feed           : calls the relevant API endpoint and return the list of posts
        primfeed post                : calls the relevant API endpoint and add a new post to the feed
        primfeed comment             : calls the relevant API endpoint and add a comment to the post whose id is <postId>
"""
