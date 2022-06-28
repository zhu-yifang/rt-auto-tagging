# rt-auto-tagging
A python script auto tags RT using Playwright

# Goal
1. Auto log in. (Done)
2. Get all unsolved tickets in the T-watch queue and CUS queue. (Done)
3. Parse tickets.
   1. Get all the content of the ticket. (Done)
   2. Parse it with regular expression and keywords mathcing. (Doing)
4. ~~Tag affliations~~, since RT has auto tagging for affliation, I will not worry about it.
5. Tag support tags with some single tickts.
6. Test it with some human tagged tickets.

# Logic of tagging
Based on the hardness of tagging
From easy to hard:
mass email = thesis = two factor = name change = no tag = phish report <
google drive = google group = library related  = virus/malware = password reset = printing <
hardware = microsoft = network <
software = reed account

Usually, we don't tag a ticket with multiple tags, but there are some cases we will do multiple tagging:
1. Microsoft Office/365 password reset ticket? Tag both microsoft and password reset.
2. Printer in the library having problems? Tag both library related and printing.
3. User having trouble printing from an Office application? Tag both microsoft and printing.
4. If thesis, no Microsoft