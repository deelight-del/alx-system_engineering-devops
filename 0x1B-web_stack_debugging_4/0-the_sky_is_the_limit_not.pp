# Puppet file to replace a line...


exec {'sed replacement':
  command  => 'sed -i "s/^ULIMIT.*/ULIMIT=\"-n 2048\"/" /etc/default/nginx',
  path     => '/bin',
  provider =>  'shell'
}
