# apache
    <VirtualHost *:32>
        DocumentRoot "/var/www/wordpress"
        ServerName 111.230.224.190

        <Directory /var/www/wordpress> 
            Options FollowSymLinks 
            AllowOverride All
            Require all granted
        </Directory>
    </VirtualHost>
