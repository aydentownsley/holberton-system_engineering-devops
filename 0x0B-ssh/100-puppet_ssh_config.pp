"100-puppet_ssh_config.pp" 15L, 272C                                                     1,1           All
#!/usr/bin/puppet
#Setting up serv to connect w/o pwd

augeas { 'id file':
  context => '/etc/ssh/ssh_config',
  changes => 'set IdentityFile ~/.ssh/holberton',
}

augeas { 'pwd auth':
  context => '/etc/ssh/ssh_config',
  changes => 'set PasswordAuthentication no',
}

