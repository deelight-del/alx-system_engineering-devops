#Puppeteering and automating adding HTTP header to our respective web servers
include stdlib

## Installing nginx
package {'nginx':
  ensure => 'installed',
}


#Define file resource for notifying
file {'default':
  path   => '/etc/nginx/sites-available/default',
  ensure => file,
}

#Replacing content in the lines of the config files
file_line {'replace a default':
  path     => '/etc/nginx/sites-available/default',
  line     => "\t\tadd_header X-Served-By \"${facts['networking']['hostname']}\";",
  after    => '^\s*location / {',
  multiple => false,
}

#Running nginx service
service {'nginx':
  ensure    => running,
  enable    => true,
  name      => 'nginx',
  require   => Package['nginx'],
  subscribe => File['default'],
}
