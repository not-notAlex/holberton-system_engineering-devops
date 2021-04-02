# kills process killmenow

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow'
}
