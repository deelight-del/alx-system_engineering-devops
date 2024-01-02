#This file contains a puppet that manages the file_line
# Include the stdlib module
require stdlib

#Other part of code
file_line { 'change password auth':
  ensure =>  present,
  path =>  '/etc/ssh/ssh_config',
  line =>  '    PasswordAuthentication no'
}

file_line { 'change Identity file':
  ensure =>  present,
  path =>  '/etc/ssh/ssh_config',
  line =>  '    IdentityFile ~/.ssh/school'
}
