# 🚀 MLflow Simple Server

Installation et déploiement rapide d'un serveur MLflow avec service systemd sur Linux.

## ✨ Fonctionnalités

- ⚡ **Installation en une commande**
- 🔄 **Service systemd intégré** (démarrage automatique)
- 🛠️ **Script de gestion simplifié**
- 📊 **Base de données SQLite intégrée**
- 🧪 **Script de test inclus**
- 🔧 **Configuration flexible**

## 🎯 Installation rapide

```bash
# Cloner le repository
git clone https://github.com/votre-username/mlflow-simple-server.git
cd mlflow-simple-server

# Rendre exécutable et installer
chmod +x setup_mlflow.sh
./setup_mlflow.sh
```

## 🌐 Accès

Une fois installé, MLflow sera accessible sur :
- **Local** : http://localhost:5000
- **Réseau** : http://votre-ip:5000

## 🛠️ Gestion du service

Le script crée automatiquement `~/mlflow/manage.sh` :

```bash
# Commandes disponibles
./manage.sh start      # Démarrer MLflow
./manage.sh stop       # Arrêter MLflow
./manage.sh restart    # Redémarrer MLflow
./manage.sh status     # Voir l'état
./manage.sh logs       # Voir les logs en temps réel
./manage.sh enable     # Activer au démarrage
./manage.sh disable    # Désactiver au démarrage
```

## 🧪 Test de l'installation

```bash
# Copier le script de test
cp scripts/test_mlflow_simple.py ~/mlflow/

# Lancer le test
cd ~/mlflow
python3 test_mlflow_simple.py
```

## 📁 Structure créée

```
~/mlflow/
├── mlflow.db              # Base de données SQLite
├── artifacts/             # Artefacts des modèles
├── manage.sh             # Script de gestion
└── test_mlflow_simple.py # Script de test (optionnel)
```

## ⚙️ Configuration avancée

Pour une configuration personnalisée, voir `config/mlflow-config.example.yml`.

## 📋 Prérequis

- **OS** : Linux (Ubuntu, Debian, CentOS, etc.)
- **Python** : 3.7+
- **Permissions** : sudo (pour le service systemd)

## 🔧 Dépannage

### Service qui ne démarre pas
```bash
# Voir les logs détaillés
sudo journalctl -u mlflow -f

# Vérifier la configuration
sudo systemctl status mlflow
```

### MLflow pas dans le PATH
```bash
# Vérifier l'installation
pip3 show mlflow
which mlflow

# Réinstaller si nécessaire
pip3 install --user --force-reinstall mlflow
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :
- Ouvrir des issues
- Proposer des améliorations
- Soumettre des pull requests

## 📄 Licence

MIT License - voir le fichier LICENSE pour plus de détails.

## 🏷️ Tags

`mlflow` `machine-learning` `ml-ops` `tracking` `systemd` `linux` `deployment`
