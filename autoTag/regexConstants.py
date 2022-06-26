import re

# filter out the CUS auto-reply
# content
autoReply = 'We have received your email with the subject'
# subject
# email

# Based on the hardness of tagging
# From easy to hard:
# mass email = thesis = two factor = name change = no tag = phish report 
# google drive = google group = library related  = virus/malware = password reset = printing
# hardware = microsoft = network
# software = reed account

# google drive
# content
'google drive'i, 'drive request'i, 'google docs'i, 'google form'i, 'google sheets'i
# subject
'Shared Drive Request'
# email

# google group
# content
'google group'i, 'group request'i, 'external users to that group'i
# subject
'Google Group Request'i, 'google group'i
# email

# hardware
# content
'iMac'i, 'hardware shop'i, 'chs'i, 'macbook pro replacement'i, 
'keyboard'i, 'monitor'i, 'battery'i, 'mouse'i
# subject
'CUS Computer Maintenance Required', 'Tracking Down'i
# email

# library related
# content
'library'i, 'IMC', 'language lab'i, 'librarian'i
# subject
'[Ask a librarian]'
# email
'er-problem-report@reed.edu'

# mass email
# content
# subject
'Message Pending'
# email

# microsoft: note, thesis template is not microsoft tag
# content
'microsoft'i, 'powerpoint'i, 'Word', 'Excel', '.doc\b', '.docx\b', 'ppt\b', 'pptx\b'
# subject
# email
'msonlineservicesteam@microsoftonline.com'
'@microsoft.com'

# network
# content
'wifi'i, 'ethernet'i, 'connection issue'i, 'reed1x'i, 'xenia'i, 'fluke'i, 
'mac address'i, 'ip address'i, 'router'i, 'switch'i, 'firewall'i, 'network'i,
'dns'i
# subject
'Wireless Maintenance'
# email

# password reset
# content
'password reset'i, 'forgot password'i, 'reset password'i, 'reset my password'i,
'account-tools'i, 'kerberos pass'i
# subject
'Kerberos password reset'i
# email
'msonlineservicesteam@microsoftonline.com'

# phish report/fwd
# content
'phish'i, 'phishing'i, 'scam'i, 'span'i
# subject
# email
'noreply-spamdigest@google.com'

# printing/copier
# content
'print'i, 'ipp.reed.edu', 'xerox'i, 'ctx'i, 'copier'i, 'laserjet'i, 'toner'i
# subject
# email
'xerox'i, 'ctx'i

# reed accounts & access
# content
'Please follow the steps below to setup your Reed account',
'new employee'i, 'new student'i, 'new faculty'i, 'kerberos'i, 'vpn'i, 'dlist'i,
'reed account'i
# subject
'Reed computing account', 'Account Closure for Graduates', 'Account Tool', 'Computing at Reed'
# email
'email-alias-request@reed.edu'

# software
# content
'OS update', 'OS upgrade'i, 'operating system'i, 
'Monterey'i, 'Big Sur'i,
'software update'i, 'software upgrade'i, 'install'i, 'uninstall'i,
'license'i, 
'zotero'i, 'latex'i, 'mathematica'i, 'GIS', 'stata'i, 'SensusAccess'i, 'JMP',
'Mnova', 'vmware'i, 'matlab'i, 
'Code42'i, 'adobe'i,'1password'i, 'rstudio'i, 
# subject
# email

# thesis
# content
'thesis'i
# subject
# email

# two-factor
# content
'duo'i, 'hardware token'i, 'two-?factor'i, 
# subject
'duo'i
# email

# user/name change
# content
'name change'i, 'change name'i, 'change username'i, 'username change'i
# subject
# email

# virus/malware
# content
'crowdstrike'i, 'virus'i, 'malware'i, 'trojan'i
# subject
'crowdstrike'i
# email
'malwarebytes.com', 'crowdstrike'

# no tag
# content
# subject
'Welcome to Reed College|Notes for your first day of work'
# email
'etrieve@reed.edu', 'schrodinger.com'

