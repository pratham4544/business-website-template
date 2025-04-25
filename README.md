
---

# 📄 README: Deploying Business Website Template on AWS EC2 (Ubuntu)

## Overview

This guide provides detailed instructions to deploy the [Business Website Template](https://github.com/pratham4544/business-website-template.git) on an AWS EC2 Ubuntu instance. The deployment process includes setting up the EC2 instance, installing necessary software, configuring the web server, and securing the site with SSL.

---

## 🔧 Prerequisites

Before starting, ensure you have:

- An AWS account with EC2 access.
- A GitHub account with access to the repository.
- Basic knowledge of SSH and command-line operations.

---

## 🚀 Step 1: Launch and Set Up Your EC2 Instance

1. **Log in to AWS Management Console**: Navigate to the [EC2 Dashboard](https://console.aws.amazon.com/ec2/).

2. **Launch Instance**:
   - Click on **Launch Instance**.
   - Choose **Ubuntu Server 20.04 LTS** (or the latest available version) as the AMI.
   - Select an instance type (e.g., `t2.micro` for free tier eligibility).
   - Configure instance details as needed.
   - Add storage if necessary.
   - **Configure Security Group**:
     - Allow inbound traffic on ports `22` (SSH), `80` (HTTP), and `443` (HTTPS).
   - **Review and Launch**:
     - Create a new key pair or use an existing one. Download and save the `.pem` file securely.

3. **Access the Instance**:
   - Once the instance is running, note its public IP address.
   - Connect via SSH:
     ```bash
     chmod 400 /path/to/your-key.pem
     ssh -i /path/to/your-key.pem ubuntu@<EC2_PUBLIC_IP>
     ```

---

## 🛠️ Step 2: Update and Install Necessary Software

1. **Update Package Lists**:
   ```bash
   sudo apt update && sudo apt upgrade -y
   ```

2. **Install Git**:
   ```bash
   sudo apt install git -y
   ```

3. **Install Nginx**:
   ```bash
   sudo apt install nginx -y
   ```

4. **Install Certbot for SSL**:
   ```bash
   sudo apt install certbot python3-certbot-nginx -y
   ```

---

## 📥 Step 3: Clone the Repository

1. **Navigate to the Web Directory**:
   ```bash
   cd /var/www/html
   ```

2. **Clone the Repository**:
   ```bash
   sudo git clone https://github.com/pratham4544/business-website-template.git .
   ```

3. **Set Appropriate Permissions**:
   ```bash
   sudo chown -R www-data:www-data /var/www/html
   sudo chmod -R 755 /var/www/html
   ```

---

## ⚙️ Step 4: Configure Nginx

1. **Remove Default Nginx Configuration**:
   ```bash
   sudo rm /etc/nginx/sites-enabled/default
   ```

2. **Create a New Nginx Configuration File**:
   ```bash
   sudo nano /etc/nginx/sites-available/business-website
   ```
   Add the following configuration:
   ```nginx
   server {
       listen 80;
       server_name <EC2_PUBLIC_IP>;

       root /var/www/html;
       index index.html;

       location / {
           try_files $uri $uri/ =404;
       }
   }
   ```

3. **Enable the New Site Configuration**:
   ```bash
   sudo ln -s /etc/nginx/sites-available/business-website /etc/nginx/sites-enabled/
   ```

4. **Test Nginx Configuration**:
   ```bash
   sudo nginx -t
   ```

5. **Restart Nginx**:
   ```bash
   sudo systemctl restart nginx
   ```

---

## 🔒 Step 5: Secure the Website with SSL

1. **Obtain an SSL Certificate**:
   ```bash
   sudo certbot --nginx -d <EC2_PUBLIC_IP>
   ```
   Follow the prompts to complete the SSL setup.

2. **Verify SSL Installation**:
   - Access your website via `https://<EC2_PUBLIC_IP>` to ensure SSL is active.

---

## 📡 Step 6: Access the Website

- Open a web browser and navigate to `http://<EC2_PUBLIC_IP>` or `https://<EC2_PUBLIC_IP>` to view your deployed website.

---

## 🔄 Optional: Set Up Domain Name

To associate a custom domain with your EC2 instance:

1. **Allocate an Elastic IP**:
   - In the EC2 Dashboard, go to **Elastic IPs** and allocate a new IP.

2. **Associate the Elastic IP with Your Instance**:
   - Select the allocated IP and associate it with your running instance.

3. **Update Domain DNS Settings**:
   - In your domain registrar's dashboard, create an A record pointing to the Elastic IP.

4. **Update Nginx Configuration**:
   - Replace `<EC2_PUBLIC_IP>` with your domain name in the Nginx configuration file:
     ```nginx
     server {
         listen 80;
         server_name yourdomain.com;
         ...
     }
     ```

5. **Restart Nginx**:
   ```bash
   sudo systemctl restart nginx
   ```

---

## 📝 Conclusion

By following these steps, you have successfully deployed the Business Website Template on your AWS EC2 Ubuntu instance. For further customization and enhancements, refer to the [official documentation](https://nginx.org/en/docs/) and [Certbot guides](https://certbot.eff.org/docs/).

---
