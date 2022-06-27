import re

# filter out the CUS auto-reply
# content
autoReply = [re.compile('We have received your email with the subject')]
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
googleDriveContent = [re.compile('google drive', re.I), re.compile('drive request', re.I),
re.compile('google form', re.I), re.compile('google sheets', re.I)]
# subject
googleDriveSubject = [re.compile('google drive', re.I), re.compile('drive request', re.I),
re.compile('google form', re.I), re.compile('google sheets', re.I), re.compile('Shared Drive Request')]
# email

# google group
# content
googleGroupContent = [re.compile('google group', re.I), re.compile('group request', re.I),
re.compile('external users to that group', re.I)]
# subject
googleGroupContent = [re.compile('google group', re.I), re.compile('group request', re.I)]
# email

# hardware
# content
hardwareContent = [re.compile('chs', re.I), re.compile('iMac', re.I), re.compile('hardware shop', re.I),
re.compile('macbook pro replacement', re.I), re.compile('keyboard', re.I), re.compile('monitor', re.I),
re.compile('battery', re.I), re.compile('mouse', re.I)]
# subject
hardwareSubject = [re.compile('CUS Computer Maintenance Required'), re.compile('Tracking Down', re.I), 
re.compile('chs', re.I), re.compile('iMac', re.I), re.compile('hardware shop', re.I),
re.compile('macbook pro replacement', re.I), re.compile('keyboard', re.I), re.compile('monitor', re.I),
re.compile('battery', re.I), re.compile('mouse', re.I)]
# email

# library related
# content
libraryContent = [re.compile('library', re.I), re.compile('IMC'), 
re.compile('language lab'), re.compile('librarian')]

# subject
librarySubject = [re.compile('\[Ask a librarian\]')]

# email
libraryEmail = [re.compile('er-problem-report@reed.edu')]


# mass email
# content
# subject
massEmailSubject = [re.compile('Message Pending')]
# email

# microsoft: note, thesis template is not microsoft tag
# content
microsoftContent = [re.compile('microsoft', re.I), re.compile('power\s?point', re.I),
re.compile('Word'), re.compile('Excel'), re.compile('\.doc'), re.compile('\.docx'),
re.compile('\bppt\b'), re.compile('\bpptx\b')]
# subject
microsoftSubject = [re.compile('microsoft', re.I), re.compile('powerpoint', re.I),
re.compile('Word'), re.compile('Excel')]
# email
microsoftEmail = [re.compile('msonlineservicesteam@microsoftonline.com'),
re.compile('@microsoft.com')]


# network
# content
networkContent = [re.compile('network', re.I), re.compile('router', re.I), re.compile('wifi', re.I),
re.compile('ethernet', re.I), re.compile('connection issue', re.I), re.compile('reed1x', re.I),
re.compile('xenia'), re.compile('fluke', re.I), re.compile('mac address', re.I), 
re.compile('ip address', re.I), re.compile('switch', re.I), re.compile('firewall', re.I),
re.compile('dns', re.I)]
# subject
networkSubject = [re.compile('Wireless Maintenance'), re.compile('network', re.I), re.compile('router', re.I),
re.compile('wifi', re.I), re.compile('ethernet', re.I), re.compile('connection issue', re.I), 
re.compile('reed1x', re.I), re.compile('xenia'), re.compile('fluke', re.I), re.compile('mac address', re.I), 
re.compile('ip address', re.I), re.compile('switch', re.I), re.compile('firewall', re.I),
re.compile('dns', re.I)]

# email

# password reset
# content
passwordResetContent = [re.compile('password reset', re.I), 
re.compile('(?:forgot|reset) (?:my|the)? password', re.I),
re.compile('account-tools', re.I), re.compile('kerberos pass', re.I)]
# subject
passwordResetSubject = [re.compile('password reset', re.I), 
re.compile('(?:forgot|reset) (?:my|the)? password', re.I),
re.compile('account-tools', re.I), re.compile('kerberos pass', re.I)]
# email
passwordResetEmail = [re.compile('msonlineservicesteam@microsoftonline.com')]

# phish report/fwd
# content
phishContent = [re.compile('phish', re.I), re.compile('scam', re.I),
re.compile('spam', re.I)]
# subject
phishSubject = [re.compile('phish', re.I), re.compile('scam', re.I),
re.compile('spam', re.I)]
# email
phishEmail = [re.compile('noreply-spamdigest@google.com')]


# printing/copier
# content
printingContent = [re.compile('print', re.I), re.compile('copier', re.I), re.compile('ipp.reed.edu'),
re.compile('xerox', re.I), re.compile('ctx', re.I), re.compile('laserjet', re.I), re.compile('toner', re.I)]
# subject
printingSubject = [re.compile('print', re.I), re.compile('copier', re.I), re.compile('ipp.reed.edu'),
re.compile('xerox', re.I), re.compile('ctx', re.I), re.compile('laserjet', re.I), re.compile('toner', re.I)]
# email
printintEmail = [re.compile('xerox', re.I), re.compile('ctx', re.I)]

# reed accounts & access
# content
accountContent = [re.compile('Please follow the steps below to setup your Reed account'), 
re.compile('new (?:employee|student|faculty)', re.I), re.compile('vpn', re.I), re.compile('dlist', re.I),
re.compile('reed account', re.I), re.compile('kerberos', re.I)]
# subject
accountSubject = [re.compile('Reed computing account'), re.compile('Account Closure for Graduates'),
re.compile('Account Tool'), re.compile('Computing at Reed')]
# email
accountEmail = [re.compile('email-alias-request@reed.edu')]

# software
# content
softwareContent = [re.compile('\bOS upgrade', re.I), re.compile('operating system', re.I), 
re.compile('Monterey'), re.compile('Big Sur', re.I), re.compile('Catalina'), re.compile('Mojave'),
re.compile('Sierra'), re.compile('software update', re.I), re.compile('software upgrade', re.I), 
re.compile('install', re.I), re.compile('uninstall', re.I), re.compile('license', re.I), 
re.compile('zotero', re.I), re.compile('latex', re.I), re.compile('mathematica', re.I), re.compile('GIS'), 
re.compile('stata', re.I), re.compile('SensusAccess', re.I), re.compile('vmware', re.I), 
re.compile('matlab', re.I), re.compile('Code42', re.I), re.compile('adobe', re.I), re.compile('1password', 
re.I), re.compile('rstudio', re.I), re.compile('\bOS update'), re.compile('JMP'), re.compile('Mnova')]
# subject
softwareSubject = [re.compile('\bOS upgrade', re.I), re.compile('operating system', re.I), 
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
thesisContent = [re.compile('thesis format', re.I)]
# subject
thesisSubject = [re.compile('thesis format', re.I)]
# email

# two-factor
# content
twoFactorContent = [re.compile('duo', re.I), 
re.compile('hardware token', re.I), re.compile('two-?factor', re.I)]
# subject
twoFactorSubject = [re.compile('duo', re.I)]
# email

# user/name change
# content
nameChangeContent = [re.compile('name change', re.I),
re.compile('change name', re.I), re.compile('change username', re.I),
re.compile('username change', re.I)]
# subject
nameChangeContent = [re.compile('name change', re.I),
re.compile('change name', re.I), re.compile('change username', re.I),
re.compile('username change', re.I)]
# email

# virus/malware
# content
virusContent = [re.compile('virus', re.I), re.compile('malware', re.I),
re.compile('trojan', re.I), re.compile('crowdstrike', re.I)]
# subject
virusSubject = [re.compile('virus', re.I), re.compile('malware', re.I),
re.compile('trojan', re.I), re.compile('crowdstrike', re.I)]
# email
virusEmail = [re.compile('malwarebytes.com'), re.compile('crowdstrike')]

# no tag
# content
# subject
noTagSubject = [re.compile('Welcome to Reed College'), 
re.compile('Notes for your first day of work')]
# email
noTagEmail = [re.compile('etrieve@reed.edu'), re.compile('schrodinger.com')]


