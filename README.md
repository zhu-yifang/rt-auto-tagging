# rt-auto-tagging
A python script auto tags RT using Playwright

# Goal
1. Auto log in. (Done)
2. Get all unsolved tickets in the T-watch queue and CUS queue. (Done)
3. Parse tickets.
   1. Get all the content of the ticket. (Done)
   2. Parse it with regular expression and keywords mathcing. (Done)
4. ~~Tag affliations~~, since RT has auto tagging for affliation, I will not worry about it. (Skip)
5. Test it with some human tagged tickets. (Doing)
6. Using it!

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

--------
[RT Support Tags Wikis](https://ciswikis.reed.edu/doku.php?id=cus:rt-support-tags&s[]=tag)

[Retroactively tagging RT tickets - January-May 2022](https://docs.google.com/spreadsheets/d/1EfZhidGR3DsxsI__mE9TmgOAjzyiR3LwHd3cO5JwIvA/edit#gid=0)

[Sam tagged tickets](https://help.reed.edu/Search/Results.html?Format=%27%3Cb%3E%3Ca%20href%3D%22__WebPath__%2FTicket%2FDisplay.html%3Fid%3D__id__%22%3E__id__%3C%2Fa%3E%3C%2Fb%3E%2FTITLE%3A%23%27%2C%0A%27%3Cb%3E%3Ca%20href%3D%22__WebPath__%2FTicket%2FDisplay.html%3Fid%3D__id__%22%3E__Subject__%3C%2Fa%3E%3C%2Fb%3E%2FTITLE%3ASubject%27%2C%0AStatus%2C%0AQueueName%2C%0AOwner%2C%0APriority%2C%0A%27__NEWLINE__%27%2C%0A%27__NBSP__%27%2C%0A%27%3Csmall%3E__Requestors__%3C%2Fsmall%3E%27%2C%0A%27%3Csmall%3E__CreatedRelative__%3C%2Fsmall%3E%27%2C%0A%27%3Csmall%3E__ToldRelative__%3C%2Fsmall%3E%27%2C%0A%27%3Csmall%3E__LastUpdatedRelative__%3C%2Fsmall%3E%27%2C%0A%27%3Csmall%3E__TimeLeft__%3C%2Fsmall%3E%27&Order=ASC%7CASC%7CASC%7CASC&OrderBy=id%7C%7C%7C&Query=Queue%20%3D%20%27cus%27%20AND%20Created%20%3C%20%272022-03-01%27%20AND%20Created%20%3E%20%272022-01-31%27%20AND%20id%20%3C%20337918&RowsPerPage=0&SavedChartSearchId=new&SavedSearchId=new)