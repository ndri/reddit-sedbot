# reddit-sedbot

Run the sed substitute command on reddit comments.

![example screenshot](https://i.imgur.com/SnAIoMs.png)

I am running it with the user [/u/\_sed\_](https://www.reddit.com/user/_sed_).

# Examples

    "i am a bad person" - /u/sad_redditor
    | "sed s/bad/good/" - /u/wholesome_redditor
    || "i am a good person" - /u/_sed_

    "sudo apt-get install gentoo" - /u/linux_redditor
    | "sed s/-get//" - /u/snarky_redditor
    || "sudo apt install gentoo" - /u/_sed_

    "my hovercraft is full of eels" - /u/casual_redditor
    | "sed s/[aeiouy]/o/g s/$/!/" - /u/cheeky_redditor
    || "mo hovorcroft os foll of ools!" - /u/_sed_

See more sed examples at http://www.grymoire.com/Unix/Sed.html

# What it does

1. Matches reddit comments that start with `sed` and include the pattern `s/pattern/replacement/flag`
2. Runs the command `echo "parent comment" | sed "s/pattern/replacement/flag"` using [subprocess.Popen](https://docs.python.org/2/library/subprocess.html)
3. Replies with the output of the command

Full regex: `/(?:\s+|^)s\/((?:[^/\\]|\\.)+)\/((?:[^/\\]|\\.)*)\/([0-9gI]*)/`

## Is it safe to let reddit run commands in your terminal?

If the `subprocess.Popen` argument `shell` was `True`, then no, absolutely not.

But since the bot doesn't have `shell = True`, the command

    echo "hello`rm -rf ~/*\`world"

prints out

    hello`rm -rf ~/*`world

and it's all good. I hope.

Don't try this command in your terminal!

# I want to run it myself for some reason

Download [praw](https://praw.readthedocs.io/en/latest/), add your API keys to the [praw.ini file](https://github.com/ndri/reddit-sedbot/blob/master/praw.ini) and run reddit-sedbot.py
