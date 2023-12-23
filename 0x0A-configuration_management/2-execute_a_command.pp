# Manifest to kill a proces
#

exec {'killmenow':
  command =>  '/usr/bin/pkill -f "killmenow"'
}
