import issue_commenter

def test_get_issue_links():

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
    links = issue_commenter.get_issue_links(issue)

    assert links == expected_links
