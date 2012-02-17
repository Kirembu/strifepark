#!/usr/bin/python2.4

'''Post a message to twitter'''

__author__ = 'in.kirembu@gmail.com'

import ConfigParser
import getopt
import os
import sys
from zerxis_twitter import twitter


def update_status(message,in_reply_to_id=None):
  consumer_keyflag = 'ih5MerLMDnRSTURoAJM4oQ'
  consumer_secretflag = 'XJ8Y59Uy1vNS5k4GjNrbSgqZAjqyGiBvFZsHMY'
  access_keyflag = '48656739-jZfVsVGHsHiqNDHN6CbzcXyoqq2UO6sXcUMVhIpI'
  access_secretflag = 'JV1driFeXOAOGUjRM8rXTGPRDR5MokcMOnHe11raA'
  encoding = None

  consumer_key = consumer_keyflag 
  consumer_secret = consumer_secretflag
  access_key = access_keyflag
  access_secret = access_secretflag

  if not consumer_key or not consumer_secret or not access_key or not access_secret:
    update_error = ("Something's missing")
  api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret,
                    access_token_key=access_key, access_token_secret=access_secret,
                    input_encoding=encoding)
  try:
    status = api.PostUpdate(message,in_reply_to_id)
  except UnicodeDecodeError:
    tweet_error = "Your message could not be encoded.  Perhaps it contains non-ASCII characters? "

  updated_status = "%s just posted: %s" % (status.user.name, status.text)

if __name__ == "__main__":
  main()
