# Puppet file that automates the process
# of installing and using nginx...

#include stdlib
include stdlib

#Install the nginx service with package resource
package {'nginx':
  name => nginx,
}

#Edit the config file to contain the redirect
file_line {'config_line':
  path  => '/etc/nginx/sites-available/default',
  line  => ' rewrite ^/redirect_me https://www.youtube.com permanent;',
  after => 'server_name _;',
}

#Create the default file for hello world
file {'var html file':
  name    => '/var/www/html/index.html',
  content => 'Hello World!',
}

#Start nginx with service.
service {'nginx':
  ensure  => true,
  name    => 'nginx',
  require => Package['nginx']
}
