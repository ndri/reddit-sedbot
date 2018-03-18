import praw, re, json
from subprocess import Popen, PIPE

regex = r"(?:\s+|^|'|\")s\/((?:[^/\\]|\\.)+)\/((?:[^/\\]|\\.)*)\/([0-9gI]*)"
footer = "\n\n---\n^^reddit ^^sedbot ^^| ^^[info](https://github.com/ndri/reddit-sedbot)"


def main():
    reddit = praw.Reddit("reddit-sedbot")
    subreddit = reddit.subreddit("all")

    with open("blacklist.json") as f:
        blacklist = json.loads(f.read())
    for sub in blacklist["disallowed"] + blacklist["permission"]:
        subreddit.filters.add(sub)

    while True:
        try:
            for comment in subreddit.stream.comments():
                text = comment.body

                if not text.lstrip("`").lstrip().startswith("sed"):
                    continue

                matches = re.findall(regex, text)

                if not matches:
                    continue
                    
                try:
                    parent = comment.parent().body.replace(footer, "")
                except:
                    print("Match but no parent: " + comment.permalink)
                    continue

                command = ["sed"]

                for match in matches:
                    command += ["-e", "s/{}/{}/{}".format(match[0], match[1], match[2])]

                echo = Popen(["echo", "-n", parent], stdout = PIPE)
                sed = Popen(command, stdin = echo.stdout, stdout = PIPE)
                reply = sed.stdout.read().decode("utf-8")

                print()
                print(comment.permalink)
                print(parent)
                print(text)
                print(reply)

                if reply != parent and comment.author != reddit.user.me():
                    if footer not in reply:
                        reply += footer
                    comment.reply(reply)

        except Exception as error:
            print(error)


if __name__ == '__main__':
    main()