# /etc/puppetlabs/code/environments/production/manifests/web_server_setup.pp

# Ensure the package 'nginx' is installed
package { 'nginx':
 ensure => installed,
}

# Ensure the directories exist
file { '/data/web_static/shared':
 ensure => directory,
 owner => 'ubuntu',
 group => 'ubuntu',
 mode   => '0755',
}

file { '/data/web_static/releases/test':
 ensure => directory,
 owner => 'ubuntu',
 group => 'ubuntu',
 mode   => '0755',
}

# Ensure the index.html file exists
file { '/data/web_static/releases/test/index.html':
 ensure => file,
 owner   => 'ubuntu',
 group   => 'ubuntu',
 mode    => '0644',
 content => '<html>
 <head>
 </head>
 <body>
    Holberton School
 </body>
</html>',
}

# Ensure the symbolic link exists
file { '/data/web_static/current':
 ensure => link,
 target => '/data/web_static/releases/test',
 owner => 'ubuntu',
 group => 'ubuntu',
}

# Ensure the nginx configuration is correct
file_line { 'nginx_static_location':
 path => '/etc/nginx/sites-enabled/default',
 line => 'location /hbnb_static { alias /data/web_static/current; index index.html; }',
 match => '^location \/hbnb_static {',
}

# Ensure nginx is running
service { 'nginx':
 ensure     => running,
 enable     => true,
 hasrestart => true,
 hasstatus => true,
 require    => Package['nginx'],
}

