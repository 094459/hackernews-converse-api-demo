# hackernews-converse-api-demo

A quick demo on how you can use generative AI to summarise dense comment threads in Hacker News, using the Amazon Bedrock Converse API.

Check out the accompanying blog post, [Save time reading Hacker News comments using Converse API](https://community.aws/content/2jhDpOY0CI1KEhKkk1GFDEYUWHd/save-time-reading-hacker-news-comments-using-converse-api)

How to use the script.

You will need to have the following:

* Access to an AWS account with permissions to access Amazon Bedrock
* Access enabled to Amazon Bedrock models (in the demo code I enabled access to Anthropic Claude Sonnet)

You run the script with a parameter, which is the news item ID which you will find on each piece of news in Hackers news.

$ python hacker_news_comments.py {itemid}

This will create a file called comments.txt in the directory where the script is run. You can now run the summariser

$ python summarise_comments.py

And it should output to the command line, the summary.