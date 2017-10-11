# reddit-sedbot

Run the sed substitute command on reddit comments.

# What it does

1. Matches reddit comments that include the pattern `s/pattern/replacement/flag` 
2. Run the command `echo "comment" | sed "s/pattern/replacement/flag"` using `[subprocess.Popen](https://docs.python.org/2/library/subprocess.html)`

## Is it safe to let reddit run commands in your terminal?

If the `subprocess.Popen` argument `shell` was `True`, then yes, absolutely.

But since the bot doesn't have `shell = True`, the command `echo "hello\`rm -rf ~/*\`world"` prints out `hello\`rm -rf ~/*\`world` and it's all good. I hope. Don't try this command in your terminal!

# I want to run it myself for some reason

Download [praw](https://praw.readthedocs.io/en/latest/), add your API keys to the [praw.ini file](https://github.com/ndri/reddit-sedbot/blob/master/praw.ini) and you're good to go.
