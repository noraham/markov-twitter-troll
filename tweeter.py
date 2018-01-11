import twitter
import os
import markov
import sys

api = twitter.Api(
    consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
    consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
    access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

print api.VerifyCredentials()

input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = markov.open_and_read_file(input_path)

# Get a Markov chain
chains = markov.make_chains(input_text)

# Produce random text
random_text = markov.make_text(chains)

# status = api.PostDirectMessage(random_text, screen_name='soylentbleen')  # this is how you send direct messages

status = api.PostUpdate(random_text)  # tweet to linked account
print status.text
