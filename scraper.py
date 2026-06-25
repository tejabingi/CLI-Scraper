import requests
def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    return response.json()
def parse_posts(posts):
    result = [] 

    for post in posts:
        result.append({
            "id" : post["id"],
            "title" : post["title"]
        })
    return result