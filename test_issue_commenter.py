from unittest.mock import patch

# TODO: mock get_issues function to return an empty list for this test
with patch('issue_commenter.get_issues', return_value=[]):
    with patch.dict('os.environ', {'GITHUB_TOKEN': 'mock_token'}):
        from issue_commenter import get_issue_links


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
    links = get_issue_links(issue)

    # Assert that the links match the expected output
    assert links == expected_links
