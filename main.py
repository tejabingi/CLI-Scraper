import argparse
import json
from scraper import fetch_posts, parse_posts

parser = argparse.ArgumentParser()

parser.add_argument (
    "--format",
    choices=["json", "text"],
    default="json"
)

parser.add_argument("--save")
args = parser.parse_args() 

posts = fetch_posts()
parsed_posts = parse_posts(posts)

if args.format == "json":
    output = json.dumps(parsed_posts, indent = 4)
    print(output)

    if args.save:
        with open(args.save, "w") as file:
            file.write(output)
    
elif args.format == "text":
    output = ""

    for post in parsed_posts:
        line = f'{post["id"]}: {post["title"]}'
        print(line)
        output += line + "\n"

    if args.save:
        with open(args.save, "w") as file:
            file.write(output)

