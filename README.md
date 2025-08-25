# MLflow sur PythonAnywhere 🚀

Déployez un serveur MLflow en 5 minutes sur PythonAnywhere.

## 📋 Installation rapide

```bash
# 1. Installer MLflow
pip3.10 install --user mlflow

# 2. Créer les dossiers
mkdir ~/mlflow_project
cd ~/mlflow_project
mkdir mlruns artifacts

# 3. Télécharger les fichiers de ce repo
wget https://raw.githubusercontent.com/votre-repo/main/wsgi.py
wget https://raw.githubusercontent.com/votre-repo/main/test.py

# 4. Modifier votre username dans wsgi.py
nano wsgi.py  # Remplacer VOTRE_USERNAME par votre vrai username

# 5. Configurer l'app web PythonAnywhere avec wsgi.py
# 6. Tester
python3.10 test.py
```

## 📁 Structure du projet

```
mlflow-pythonanywhere/
├── README.md       # Ce guide
├── wsgi.py         # Configuration pour PythonAnywhere  
└── test.py         # Script de test
```

C'est tout ! 🎉

## 📖 Guide détaillé

### Étape 1 : Préparation
1. Créez un compte sur [pythonanywhere.com](https://www.pythonanywhere.com)
2. Ouvrez une console Bash

### Étape 2 : Installation
```bash
# Installer MLflow
pip3.10 install --user mlflow

# Créer les dossiers
mkdir ~/mlflow_project
cd ~/mlflow_project
mkdir mlruns artifacts
```

### Étape 3 : Configuration Web App
1. Onglet **Web** → **Add a new web app**
2. Choisir **Manual configuration** → **Python 3.10**
3. Dans la section **Code**, cliquer sur votre fichier WSGI
4. **Remplacer tout le contenu** par le code du fichier `wsgi.py`
5. **⚠️ Modifier `VOTRE_USERNAME`** par votre vrai nom d'utilisateur
6. **Working directory** : `/home/votreusername/mlflow_project`
7. Cliquer **Reload**

### Étape 4 : Test
```bash
# Tester l'installation
python3.10 test.py
```

Visitez `https://votreusername.pythonanywhere.com` → Vous devriez voir MLflow ! 🎉

## 🔧 Utilisation

### Depuis votre machine locale
```python
import mlflow

# Se connecter à votre serveur
mlflow.set_tracking_uri("https://votreusername.pythonanywhere.com")

# Logger une expérience
with mlflow.start_run():
    mlflow.log_metric("accuracy", 0.95)
    mlflow.log_param("model", "RandomForest")
```

### Depuis PythonAnywhere
```python
import mlflow
import os

# Configuration locale
username = "votre_username"
mlflow.set_tracking_uri(f"file:///home/{username}/mlflow_project/mlruns")

# Logger une expérience
with mlflow.start_run():
    mlflow.log_metric("loss", 0.25)
```

## 🚨 Dépannage

**Erreur "Internal Server Error"** :
- Vérifiez que vous avez changé `VOTRE_USERNAME` dans wsgi.py
- Regardez les logs : Onglet Web → Error log

**MLflow ne s'affiche pas** :
```bash
# Réinstaller
pip3.10 uninstall mlflow
pip3.10 install --user mlflow
```

**Permissions** :
```bash
chmod -R 755 ~/mlflow_project
```

---

**C'est tout ! Votre serveur MLflow est prêt en 3 fichiers seulement** ⚡