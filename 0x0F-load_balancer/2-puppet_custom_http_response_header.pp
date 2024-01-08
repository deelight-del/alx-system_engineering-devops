#Puppeteering and automating adding HTTP header to our respective web servers
include stdlib

## Installing haproxy
package {'haproxy':
  ensure => 'installed'
}

#Replacing content in the lines of the config files
file_line {'default':
  path     => '/etc/nginx/sites-available/default',
  line     => "\t\tadd_header X-Served-By \"${facts['networking']['hostname']}\";",
  after    => '^\s*location / {',
  multiple => false,
}

#Executing haproxy
exec {'haproxy':
  command => '/etc/init.d/haproxy restart',
  require => Package['haproxy']
}
