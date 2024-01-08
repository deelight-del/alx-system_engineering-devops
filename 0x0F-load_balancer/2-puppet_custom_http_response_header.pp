#Puppeteering and automating adding HTTP header to our respective web servers
include stdlib

file_line {'default':
  path     => '/etc/nginx/sites-available/default',
  line     => "\t\tadd_header X-Served-By \"${facts['networking']['hostname']}\"",
  after    => '^\s*location / {',
  multiple => false,
}
