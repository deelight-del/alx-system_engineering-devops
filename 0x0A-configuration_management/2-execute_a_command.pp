# Manifest to kill a proces
#

exec {'killmenow':
  command =>  'pkill -f "killmenow"'
}
