from app import db, Posts


def CreatePost(post_content, post_name, post_description, post_date, post_header_tags):

    try:

        db.session.add(
            Posts(
                post_content=post_content,
                post_name=post_name,
                post_short_desc=post_description,
                post_creation_date=post_date,
                post_header_tags=post_header_tags
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


def UpdatePost(id, content, post_name, post_description, post_creation_date, post_header_tags):

    try:

        post = Posts.query.get_or_404(id)

        post.content = content
        post.post_name = post_name
        post.post_short_desc = post_description
        post.post_creation_date = post_date,
        post.post_header_tags = post_header_tags

        db.commit()

    except:

        print("Error preforming 'UpdatePost'")

# ============================================================================================ #
# ============================================================================================ #
# ============================================================================================ #
# ============================================================================================ #
# ============================================================================================ #
# SELF TESTING: This file is used to update the database as in create new posts, delete posts or
#               update existing posts.

CreatePost(
    post_content="test",
    post_name="Initial Blog!",
    post_short_desc="Welcome to my blog, where I will be publishing my own articles.",
    post_date="28 August 2021",
    post_header_tags="""<meta desciption="First blog!" />"""
)