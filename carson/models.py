import sys
import json
from django.db import models
from carson.utils import parse_created_at
from carson.managers import TrustedManager, UntrustedManager

class Account(models.Model):
    twitter_username = models.CharField("Username", help_text="Minus the '@' sign", max_length=32)
    twitter_id = models.PositiveIntegerField("Twitter ID", editable=False, null=True)

    def __unicode__(self):
        return u"@%s" % self.twitter_username

class Tag(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class Tweet(models.Model):
    account = models.ForeignKey(Account, null=True, related_name="tweets")
    tweet_id = models.BigIntegerField()
    timestamp = models.DateTimeField()
    text = models.TextField()

    objects = models.Manager()
    trusted = TrustedManager()
    untrusted = UntrustedManager()

    def __unicode__(self):
        return u"#%d" % self.tweet_id

    class Meta:
        ordering = ["-timestamp"]

    @classmethod
    def add(cls, tweet, twitter_ids):
        # Only load if passed a string
        if isinstance(tweet, basestring):
            tweet = json.loads(tweet)

        values = {
            "tweet_id"  : tweet['id'],
            "timestamp" : parse_created_at(tweet['created_at']),
            "text"      : tweet['text'],
        }

        twitter_id = tweet['user']['id']

        if twitter_id in twitter_ids:
            account = Account.objects.get(twitter_id=twitter_id)
        else:
            account = None

        values['account'] = account

        sys.stdout.write("Added #%d\r" % tweet['id'])
        sys.stdout.flush()

        return cls.objects.create(**values)
