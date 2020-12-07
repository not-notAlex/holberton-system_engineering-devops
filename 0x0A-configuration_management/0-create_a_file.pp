# creates file in the tmp folder

file { '/tmp/holberton':
  path    => '/tmp/holberton',
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data'
}
