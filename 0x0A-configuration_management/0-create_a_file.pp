# creates file in the tmp folder

file { '/tmp/holberton':
  ensure  => file,
  path    => '/tmp/holberton',
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data'
}
