import requests
def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        print("Request timed out")

    except requests.exceptions.ConnectionError:
        print("Connection failed")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

    return []

def parse_posts(posts):
    result = [] 

    for post in posts:
        result.append({
            "id" : post["id"],
            "title" : post["title"]
        })
    return result