from scraper import parse_posts
def test_parse_posts():
    sample_data = [
        {
            "id" : 1,
            "title" : "Test title",
            "body" : "Test body"
        }
    ]
    result = parse_posts(sample_data)
    assert result == [
        {
            "id" : 1,
            "title" : "Test title"
        }
    ]