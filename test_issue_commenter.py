from unittest.mock import patch

# Mock the environment variable
with patch.dict('os.environ', {'GITHUB_TOKEN': 'mock_token'}):
    import issue_commenter

# BUG issue_commander fails on import if there is no GITHUB_TOKEN environment variable.
# We're mocking the GITHUB_TOKEN environment variable to avoid this error.

def test_get_issue_links_with_mock_token():
    # Define test variables
    issue = {
        "title": "Test Issue Title",
        "body": "Test Issue Body",
        "comments": [
            {
                "body": "Test Comment 1"
            },
            {
                "body": "Test Comment 2"
            }
        ]
    }

    expected_links = ["http://fake.stack.exchange.com/aaaa", "http://fake.stackexchange.com/bbbb"]

    # Call the function to get links
    links = issue_commenter.get_issue_links(issue)

    # Assert that the links match the expected output
    assert links == expected_links
