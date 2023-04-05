import stackexchange
import os
import openai

# First, set up the Stack Exchange API with your access token
so = stackexchange.Site(stackexchange.StackOverflow, os.environ["STACK_EXCHANGE_ACCESS_TOKEN"])

# Define a prompt for ChatGPT to generate text from
prompt = """
Here's an issue from the GitHub repository:

Title: {}

Body: {}

Comments: {}

Suggest a fix or refactoring task for this issue:

Here are some Stack Overflow posts that may be helpful:

{}
"""

# Iterate over the issues and add a comment with relevant Stack Overflow links for each one
for issue in issues:
    title = issue.title
    body = issue.body
    comments = issue.get_comments()
    comment_text = ""
    for comment in comments:
        comment_text += comment.body + " "
    prompt_text = prompt.format(title, body, comment_text, "")
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt_text,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        suggested_fix = response.choices[0].text.strip()
        # Search for relevant Stack Overflow posts
        search_results = so.search(suggested_fix)
        # Collect links to the top 3 search results
        links = [result.link for result in search_results[:3]]
        # Check if the issue already has a comment with Stack Overflow links
        has_comment = False
        for comment in issue.get_comments():
            if "Stack Overflow posts that may be helpful:" in comment.body:
                has_comment = True
                break
        # If the issue doesn't already have a comment with Stack Overflow links, add one
        if not has_comment:
            issue.create_comment("Here are some Stack Overflow posts that may be helpful:\n\n" + "\n".join(links))
    except Exception as e:
        print(f"Error occurred while generating response for issue {issue.number}: {e}")

