# 📖 Instructions d'installation détaillées

## 🎯 Installation standard

### 1. Préparation
```bash
# Mise à jour du système
sudo apt update && sudo apt upgrade -y  # Ubuntu/Debian
# ou
sudo yum update -y                       # CentOS/RHEL

# Installation de Python et pip
sudo apt install python3 python3-pip -y  # Ubuntu/Debian
# ou
sudo yum install python3 python3-pip -y   # CentOS/RHEL
```

### 2. Clonage et installation
```bash
git clone https://github.com/votre-username/mlflow-simple-server.git
cd mlflow-simple-server
chmod +x setup_mlflow.sh
./setup_mlflow.sh
```

## 🐳 Installation avec Docker (alternative)

```bash
# Créer le Dockerfile
cat > Dockerfile << 'EOF'
FROM python:3.9-slim

RUN pip install mlflow
WORKDIR /mlflow
RUN mkdir -p artifacts

EXPOSE 5000
CMD ["mlflow", "ui", "--backend-store-uri", "sqlite:///mlflow/mlflow.db", "--default-artifact-root", "/mlflow/artifacts", "--host", "0.0.0.0", "--port", "5000"]
EOF

# Builder et lancer
docker build -t mlflow-server .
docker run -p 5000:5000 -v $(pwd)/mlflow_data:/mlflow mlflow-server
```

## ☁️ Déploiement cloud

### AWS EC2
```bash
# Sur une instance EC2 Ubuntu
sudo apt update
sudo apt install git python3 python3-pip -y
git clone https://github.com/votre-username/mlflow-simple-server.git
cd mlflow-simple-server
./setup_mlflow.sh

# Ouvrir le port 5000 dans le Security Group AWS
```

### Google Cloud Platform
```bash
# Sur une VM GCP
sudo apt update
sudo apt install git python3 python3-pip -y
git clone https://github.com/votre-username/mlflow-simple-server.git
cd mlflow-simple-server
./setup_mlflow.sh

# Ouvrir le port 5000 dans le firewall
gcloud compute firewall-rules create mlflow-server --allow tcp:5000
```

## 🔐 Configuration avec authentification

Pour activer l'authentification basique :

```bash
# Installer le plugin d'authentification
pip3 install --user mlflow[extras]

# Modifier le service systemd
sudo systemctl edit mlflow

# Ajouter dans l'override :
[Service]
ExecStart=
ExecStart=/home/$USER/.local/bin/mlflow server --backend-store-uri sqlite:///home/$USER/mlflow/mlflow.db --default-artifact-root /home/$USER/mlflow/artifacts --host 0.0.0.0 --port 5000 --app-name basic-auth
Environment="MLFLOW_AUTH_CONFIG_PATH=/home/$USER/mlflow/basic_auth.ini"
```

## 🔧 Configuration avec base de données externe

### PostgreSQL
```bash
# Installation PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Création de la base
sudo -u postgres createdb mlflow
sudo -u postgres createuser mlflow
sudo -u postgres psql -c "ALTER USER mlflow PASSWORD 'votre_mot_de_passe';"

# Installation du driver Python
pip3 install --user psycopg2-binary

# Modification du service
sudo systemctl edit mlflow
# Remplacer sqlite:// par postgresql://mlflow:password@localhost:5432/mlflow
```

### MySQL
```bash
# Installation MySQL
sudo apt install mysql-server -y

# Configuration
sudo mysql -e "CREATE DATABASE mlflow;"
sudo mysql -e "CREATE USER 'mlflow'@'localhost' IDENTIFIED BY 'votre_mot_de_passe';"
sudo mysql -e "GRANT ALL PRIVILEGES ON mlflow.* TO 'mlflow'@'localhost';"

# Installation du driver
pip3 install --user PyMySQL

# URI: mysql+pymysql://mlflow:password@localhost:3306/mlflow
```

## 🌐 Configuration avec proxy reverse (Nginx)

```bash
# Installation Nginx
sudo apt install nginx -y

# Configuration
sudo tee /etc/nginx/sites-available/mlflow << 'EOF'
server {
    listen 80;
    server_name votre-domaine.com;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF

# Activation
sudo ln -s /etc/nginx/sites-available/mlflow /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl restart nginx
```

## 🔒 Sécurisation avec SSL (Let's Encrypt)

```bash
# Installation Certbot
sudo apt install certbot python3-certbot-nginx -y

# Obtention du certificat
sudo certbot --nginx -d votre-domaine.com

# Renouvellement automatique
sudo crontab -e
# Ajouter : 0 12 * * * /usr/bin/certbot renew --quiet
```

## ⚠️ Dépannage courant

### Erreur de permissions
```bash
# Vérifier les permissions du dossier
ls -la ~/mlflow
sudo chown -R $USER:$USER ~/mlflow
```

### Port déjà utilisé
```bash
# Voir qui utilise le port 5000
sudo netstat -tlnp | grep :5000
sudo lsof -i :5000

# Changer le port dans le service
sudo systemctl edit mlflow
```

### Service qui ne démarre pas
```bash
# Logs détaillés
sudo journalctl -u mlflow -n 50
sudo systemctl status mlflow -l

# Test manuel
cd ~/mlflow
~/.local/bin/mlflow ui --backend-store-uri sqlite:///$(pwd)/mlflow.db
```