def test_create_prompt():
    title = "Test issue title"
    body = "Test issue body"
    comments = ["Comment 1", "Comment 2"]
    prompt = create_prompt(title, body, comments)
    expected_prompt = f"""
Here's an issue from the GitHub repository:

Title: {title}

Body: {body}

Comments: {' '.join(comments)}

Suggest a fix or refactoring task for this issue:

Here are some Stack Overflow posts that may be helpful:

{{}}
"""
    assert prompt == expected_prompt


def test_response_generation():
    pass

def test_comment_addition():
    pass

def test_exception_handling():
    pass
