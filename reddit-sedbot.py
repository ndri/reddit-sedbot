import praw, re
from subprocess import Popen, PIPE

regex = r"(?:\s+|^)s\/((?:[^/\\]|\\.)+)\/((?:[^/\\]|\\.)*)\/([0-9gI]*)"

reddit = praw.Reddit("bot1")
subreddit = reddit.subreddit("all")

footer = "\n\n---\n^^reddit ^^sedbot ^^| ^^[info](https://github.com/ndri/reddit-sedbot)"

for comment in subreddit.stream.comments():
    text = comment.body
    matches = re.findall(regex, text)

    if matches:
        try:
            parent = comment.parent().body
        except:
            print("Match but no parent: " + comment.permalink())
            continue

        command = ["sed"]

        for match in matches:
            command += ["-e", "s/{}/{}/{}".format(match[0], match[1], match[2])]

        echo = Popen(["echo", "-n", parent], stdout = PIPE)
        sed = Popen(command, stdin = echo.stdout, stdout = PIPE)
        reply = sed.stdout.read().decode("utf-8")

        print()
        print(parent)
        print(text)
        print(reply)

        if reply != parent:
            comment.reply(reply + footer)
