# Deployment: Enabling HTTPS with Nginx

1. **Obtain an SSL certificate** (e.g., using Let's Encrypt):
   ```
   sudo certbot --nginx -d your-domain.com
   ```

2. **Update your Nginx configuration** to support HTTPS:
   ```
   server {
       listen 443 ssl;
       server_name your-domain.com;

       ssl_certificate /etc/letsencrypt/live/your-domain.com/fullchain.pem;
       ssl_certificate_key /etc/letsencrypt/live/your-domain.com/privkey.pem;

       location / {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Forwarded-Proto $scheme;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       }
   }

   # Redirect HTTP to HTTPS
   server {
       listen 80;
       server_name your-domain.com;
       return 301 https://$host$request_uri;
   }
   ```

3. **Reload Nginx**:
   ```
   sudo systemctl reload nginx
   ```

4. **Verify HTTPS is enabled** and HTTP redirects to HTTPS.