import argparse
from scraper import get_posts

parser = argparse.ArgumentParser()

parser.add_argument("--titles", action = "store_true")

args = parser.parse_args() 

posts = get_posts()
if args.titles:
    for post in posts:
        print(post["title"])