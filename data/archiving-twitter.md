---
title: Archiving Twitter
---

Twitter data is only available via the search API for up to 7 days. Data for a given account only goes back a few thousand tweets. Thus archiving tweets can be a useful activity. This entry details a few options and in the process shows some neat tips and tricks for pulling down data.

Using Google Reader
-------------------

Twitter still gives out Atom/RSS feeds (though they are increasingly hidden!).

You can thus use Google Reader, or any other feed reader with auto-archiving capabilities, to archive your twitter feed.

### Constructing the query


You need to escape non-ascii characters in the query. E.g. Here's a query for `#okfn`:

http://search.twitter.com/search.atom?q=%23okfn

Here's one for tweets @okfn:

http://search.twitter.com/search.atom?q=%40okfn

Here are tweets from `@okfn` (query is `from:okfn`):

http://search.twitter.com/search.atom?q=from%3Aokfn

### Add it on your Google Reader Account

Sign in or sign up and then add the link provided above. Archiving will now continue.


Using Javascript and the DataHub
--------------------------------

See https://github.com/OKFN-BR/BusaoSP/blob/master/getdata.js
