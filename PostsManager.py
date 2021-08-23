from app import db, Posts


def CreatePost(post_content, post_name, post_description, post_date):

    try:

        db.session.add(
            Posts(
                post_content=post_content,
                post_name=post_name,
                post_short_desc=post_description,
                post_creation_date=post_date
            )
        )
        db.session.commit()

    except:

        print("Error preforming 'CreatePost'")


def DeletePost(id):

    try:

        db.session.delete(Posts.get_or_404(id))
        db.session.commit()

    except:

        print("Error preforming 'DeletePost'")


def UpdatePost(id, content, post_name, post_description):

    try:

        post = Posts.query.get_or_404(id)

        post.content = content
        post.post_name = post_name
        post.post_short_desc = post_description

        db.commit()

    except:

        print("Error preforming 'UpdatePost'")


CreatePost(
    post_content="test",
    post_name="Initial Blog!",
    post_short_desc="Welcome to my blog, where I will be publishing my own articles.",
    post_date="28 August 2021"
)

# myvar = Posts(
#     post_content="test",
#     post_name="Initial Blog!",
#     post_short_desc="Welcome to my blog, where I will be publishing my own articles."
#     post_date="28 August 2021"
# )
# db.session.add(myvar)
# db.session.commit()