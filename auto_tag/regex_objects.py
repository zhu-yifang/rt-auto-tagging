import re
'''
模块的说明文档放在这里
'''
# filter out the CUS auto-reply
# content
auto_reply = [re.compile('We have received your email with the subject')]
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
google_drive_content = [re.compile('google drive', re.I), re.compile('drive request', re.I),
re.compile('google form', re.I), re.compile('google sheets', re.I)]
# subject
google_drive_subject = [re.compile('google drive', re.I), re.compile('drive request', re.I),
re.compile('google form', re.I), re.compile('google sheets', re.I), re.compile('Shared Drive Request')]
# email

# google group
# content
google_group_content = [re.compile('google group', re.I), re.compile('group request', re.I),
re.compile('external users to that group', re.I)]
# subject
google_group_subject = [re.compile('google group', re.I), re.compile('group request', re.I)]
# email

# hardware
# content
hardware_content = [re.compile('chs', re.I), re.compile('iMac', re.I), re.compile('hardware shop', re.I),
re.compile('macbook pro replacement', re.I), re.compile('keyboard', re.I), re.compile('monitor', re.I),
re.compile('battery', re.I), re.compile('mouse', re.I)]
# subject
hardware_subject = [re.compile('CUS Computer Maintenance Required'), re.compile('Tracking Down', re.I), 
re.compile('chs', re.I), re.compile('iMac', re.I), re.compile('hardware shop', re.I),
re.compile('macbook pro replacement', re.I), re.compile('keyboard', re.I), re.compile('monitor', re.I),
re.compile('battery', re.I), re.compile('mouse', re.I)]
# email

# library related
# content
library_content = [re.compile('library', re.I), re.compile('IMC'), 
re.compile('language lab'), re.compile('librarian')]

# subject
library_subject = [re.compile('\[Ask a librarian\]')]

# email
library_email = [re.compile('er-problem-report@reed.edu')]


# mass email
# content
# subject
mass_email_subject = [re.compile('Message Pending')]
# email

# microsoft: note, thesis template is not microsoft tag
# content
microsoft_content = [re.compile('microsoft', re.I), re.compile('power\s?point', re.I),
re.compile('Word'), re.compile('Excel'), re.compile('\.doc'), re.compile('\.docx'),
re.compile('\bppt\b'), re.compile('\bpptx\b')]
# subject
microsoft_subject = [re.compile('microsoft', re.I), re.compile('power\s?point', re.I),
re.compile('Word'), re.compile('Excel')]
# email
microsoft_email = [re.compile('msonlineservicesteam@microsoftonline.com'),
re.compile('@microsoft.com')]


# network
# content
network_content = [re.compile('network', re.I), re.compile('router', re.I), re.compile('wifi', re.I),
re.compile('ethernet', re.I), re.compile('connection issue', re.I), re.compile('reed1x', re.I),
re.compile('xenia'), re.compile('fluke', re.I), re.compile('mac address', re.I), 
re.compile('ip address', re.I), re.compile('switch', re.I), re.compile('firewall', re.I),
re.compile('dns', re.I)]
# subject
network_subject = [re.compile('Wireless Maintenance'), re.compile('network', re.I), re.compile('router', re.I),
re.compile('wifi', re.I), re.compile('ethernet', re.I), re.compile('connection issue', re.I), 
re.compile('reed1x', re.I), re.compile('xenia'), re.compile('fluke', re.I), re.compile('mac address', re.I), 
re.compile('ip address', re.I), re.compile('switch', re.I), re.compile('firewall', re.I),
re.compile('dns', re.I)]

# email

# password reset
# content
password_reset_content = [re.compile('password reset', re.I), 
re.compile('(?:forgot|reset) (?:my|the)? password', re.I),
re.compile('account-tools', re.I), re.compile('kerberos pass', re.I)]
# subject
password_reset_subject = [re.compile('password reset', re.I), 
re.compile('(?:forgot|reset) (?:my|the)? password', re.I),
re.compile('account-tools', re.I), re.compile('kerberos pass', re.I)]
# email
password_reset_email = [re.compile('msonlineservicesteam@microsoftonline.com')]

# phish report/fwd
# content
phish_content = [re.compile('phish', re.I), re.compile('scam', re.I),
re.compile('spam', re.I)]
# subject
phish_subject = [re.compile('phish', re.I), re.compile('scam', re.I),
re.compile('spam', re.I)]
# email
phish_email = [re.compile('noreply-spamdigest@google.com')]


# printing/copier
# content
printing_content = [re.compile('print', re.I), re.compile('copier', re.I), re.compile('ipp.reed.edu'),
re.compile('xerox', re.I), re.compile('ctx', re.I), re.compile('laserjet', re.I), re.compile('toner', re.I)]
# subject
printing_subject = [re.compile('print', re.I), re.compile('copier', re.I), re.compile('ipp.reed.edu'),
re.compile('xerox', re.I), re.compile('ctx', re.I), re.compile('laserjet', re.I), re.compile('toner', re.I)]
# email
printint_email = [re.compile('xerox', re.I), re.compile('ctx', re.I)]

# reed accounts & access
# content
account_content = [re.compile('Please follow the steps below to setup your Reed account'), 
re.compile('new (?:employee|student|faculty)', re.I), re.compile('vpn', re.I), re.compile('dlist', re.I),
re.compile('reed account', re.I), re.compile('kerberos', re.I)]
# subject
account_subject = [re.compile('Reed computing account'), re.compile('Account Closure for Graduates'),
re.compile('Account Tool'), re.compile('Computing at Reed')]
# email
account_email = [re.compile('email-alias-request@reed.edu')]

# software
# content
software_content = [re.compile('\bOS upgrade', re.I), re.compile('operating system', re.I), 
re.compile('Monterey'), re.compile('Big Sur', re.I), re.compile('Catalina'), re.compile('Mojave'),
re.compile('Sierra'), re.compile('software update', re.I), re.compile('software upgrade', re.I), 
re.compile('install', re.I), re.compile('uninstall', re.I), re.compile('license', re.I), 
re.compile('zotero', re.I), re.compile('latex', re.I), re.compile('mathematica', re.I), re.compile('GIS'), 
re.compile('stata', re.I), re.compile('SensusAccess', re.I), re.compile('vmware', re.I), 
re.compile('matlab', re.I), re.compile('Code42', re.I), re.compile('adobe', re.I), re.compile('1password', 
re.I), re.compile('rstudio', re.I), re.compile('\bOS update'), re.compile('JMP'), re.compile('Mnova')]
# subject
software_subject = [re.compile('\bOS upgrade', re.I), re.compile('operating system', re.I), 
re.compile('Monterey'), re.compile('Big Sur', re.I), re.compile('Catalina'), re.compile('Mojave'),
re.compile('Sierra'), re.compile('software update', re.I), re.compile('software upgrade', re.I), 
re.compile('install', re.I), re.compile('uninstall', re.I), re.compile('license', re.I), 
re.compile('zotero', re.I), re.compile('latex', re.I), re.compile('mathematica', re.I), re.compile('GIS'), 
re.compile('stata', re.I), re.compile('SensusAccess', re.I), re.compile('vmware', re.I), 
re.compile('matlab', re.I), re.compile('Code42', re.I), re.compile('adobe', re.I), re.compile('1password', 
re.I), re.compile('rstudio', re.I), re.compile('\bOS update'), re.compile('JMP'), re.compile('Mnova')]
# email

# thesis format
# content
thesis_content = [re.compile('thesis format', re.I)]
# subject
thesis_subject = [re.compile('thesis format', re.I)]
# email

# two-factor
# content
two_factor_content = [re.compile('duo', re.I), 
re.compile('hardware token', re.I), re.compile('two-?factor', re.I)]
# subject
two_factor_subject = [re.compile('duo', re.I)]
# email

# user/name change
# content
name_change_content = [re.compile('name change', re.I),
re.compile('change name', re.I), re.compile('change username', re.I),
re.compile('username change', re.I)]
# subject
name_change_subject = [re.compile('name change', re.I),
re.compile('change name', re.I), re.compile('change username', re.I),
re.compile('username change', re.I)]
# email

# virus/malware
# content
virus_content = [re.compile('virus', re.I), re.compile('malware', re.I),
re.compile('trojan', re.I), re.compile('crowdstrike', re.I)]
# subject
virus_subject = [re.compile('virus', re.I), re.compile('malware', re.I),
re.compile('trojan', re.I), re.compile('crowdstrike', re.I)]
# email
virus_email = [re.compile('malwarebytes.com'), re.compile('crowdstrike')]

# no tag
# content
# subject
no_tag_subject = [re.compile('Welcome to Reed College'), 
re.compile('Notes for your first day of work')]
# email
no_tag_email = [re.compile('etrieve@reed.edu'), re.compile('schrodinger.com')]
