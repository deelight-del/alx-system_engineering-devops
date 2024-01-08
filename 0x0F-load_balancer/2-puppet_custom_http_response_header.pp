#Puppeteering and automating adding HTTP header to our respective web servers
include stdlib

## Installing nginx
package {'nginx':
  ensure => 'installed'
}

#Replacing content in the lines of the config files
file_line {'default':
  path     => '/etc/nginx/sites-available/default',
  line     => "\t\tadd_header X-Served-By \"${facts['networking']['hostname']}\";",
  after    => '^\s*location / {',
  multiple => false,
}

#Executing nginx
exec {'nginx':
  command => '/etc/init.d/nginx restart',
  require => Package['nginx']
}
