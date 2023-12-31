#This file contains a puppet that manages the file_line
#resource of the ssh client side config file.

mod 'saz-ssh', '11.2.0'

class { 'ssh::client':
  storeconfigs_enabled =>  false,
  options              => {
    'Host *' => {
      'IdentityFile'           => '~/.ssh/school',
      'PasswordAuthentication' => 'no'
    }
  }
}
