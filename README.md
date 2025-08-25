# MLflow sur PythonAnywhere 🚀

**Déployez un serveur MLflow gratuit en 10 minutes, accessible 24h/24 depuis n'importe où !**

MLflow est un outil essentiel pour le machine learning qui permet de suivre vos expériences, comparer vos modèles et partager vos résultats. Ce guide vous montre comment créer votre propre serveur MLflow gratuit sur PythonAnywhere.

![](https://cdn.static-media.blent.ai/photos/blog/mle_article5.png)

## 🎯 Que fait ce projet ?

- **🌐 Serveur MLflow accessible depuis internet** : `https://votreusername.pythonanywhere.com`
- **💾 Stockage permanent** de vos expériences et modèles
- **👥 Partage facile** avec votre équipe ou clients
- **🔄 Synchronisation** entre vos projets locaux et le serveur
- **📊 Interface graphique** pour visualiser vos expériences

## 📁 Structure ultra-simple

```
mlflow-simple-server/
├── README.md    # Ce guide complet
├── wsgi.py      # Configuration serveur (1 seul changement à faire !)
└── test.py      # Script de test automatique
```

Seulement **3 fichiers** - pas de complexité inutile !

## 🚀 Installation express (5 minutes)

Si vous êtes pressé, suivez ces étapes rapides :

```bash
# 1. Installer MLflow
pip3.10 install --user mlflow

# 2. Créer les dossiers
mkdir ~/mlflow_project && cd ~/mlflow_project
mkdir mlruns artifacts

# 3. Télécharger wsgi.py et test.py de ce repo
# 4. Modifier votre username dans wsgi.py
# 5. Configurer l'app web avec wsgi.py
# 6. Tester avec : python3.10 test.py
```

**Mais je recommande fortement de suivre le guide détaillé ci-dessous ! 👇**

---

## 📖 Guide détaillé étape par étape

### 🎬 Avant de commencer

**Qu'est-ce que PythonAnywhere ?**
PythonAnywhere est une plateforme cloud qui offre un hébergement Python gratuit. Parfait pour héberger un serveur MLflow sans coût et sans configuration serveur complexe.

**Prérequis :**
- 10 minutes de votre temps
- Une adresse email (pour créer le compte PythonAnywhere)
- Aucune connaissance technique avancée requise !

### Étape 1 : Créer votre compte PythonAnywhere

#### 1.1 Inscription
1. Allez sur [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Cliquez sur **"Create a Beginner account"** (gratuit !)
3. Remplissez le formulaire :
   - **Username** : Choisissez bien, ce sera dans l'URL de votre serveur
   - **Email** : Votre adresse email
   - **Password** : Un mot de passe sécurisé
4. Cliquez sur **"Create account"**
5. Validez votre email si demandé

#### 1.2 Première connexion
1. Connectez-vous à votre compte
2. Vous arrivez sur le **Dashboard** - c'est votre tableau de bord
3. Familiarisez-vous avec les onglets : **Consoles**, **Web**, **Files**

### Étape 2 : Installer MLflow

#### 2.1 Ouvrir une console
1. Cliquez sur l'onglet **"Consoles"** en haut
2. Sous "Start a new console", cliquez sur **"Bash"**
3. Une nouvelle console s'ouvre - c'est votre terminal Linux !

#### 2.2 Vérifier Python
Tapez cette commande pour vérifier que Python fonctionne :
```bash
python3 --version
```
Vous devriez voir quelque chose comme `Python 3.10.x`. ✅

#### 2.3 Installer MLflow
```bash
pip3.10 install --user mlflow
```
**⏱️ Attendez 1-2 minutes** pendant l'installation.

#### 2.4 Vérifier l'installation
```bash
mlflow --version
```
Si vous voyez un numéro de version, c'est parfait ! ✅

**🔧 En cas d'erreur :**
- Si `mlflow --version` ne fonctionne pas, redémarrez votre console
- Si l'installation échoue, essayez : `pip3.10 install --user --upgrade mlflow`

### Étape 3 : Créer la structure de fichiers

#### 3.1 Créer le dossier principal
```bash
mkdir ~/mlflow_project
cd ~/mlflow_project
```
Vous créez un dossier `mlflow_project` dans votre répertoire personnel.

#### 3.2 Créer les sous-dossiers
```bash
mkdir mlruns
mkdir artifacts
```
- `mlruns` : Stockera vos expériences MLflow
- `artifacts` : Stockera vos modèles et fichiers

#### 3.3 Vérifier la création
```bash
ls -la
```
Vous devriez voir vos deux dossiers créés. ✅

### Étape 4 : Configurer le fichier WSGI

#### 4.1 Comprendre le fichier WSGI
Le fichier WSGI est le "pont" entre PythonAnywhere et MLflow. C'est lui qui dit à PythonAnywhere comment lancer votre serveur MLflow.

#### 4.2 Télécharger le fichier wsgi.py
Deux options :

**Option A - Téléchargement direct :**
```bash
wget https://raw.githubusercontent.com/votre-repo/main/wsgi.py
```

**Option B - Création manuelle :**
```bash
nano wsgi.py
```
Puis copiez le contenu du fichier `wsgi.py` de ce repository.

#### 4.3 Modifier le nom d'utilisateur
**⚠️ ÉTAPE CRUCIALE ⚠️**

Ouvrez le fichier pour modification :
```bash
nano wsgi.py
```

Trouvez cette ligne :
```python
username = "VOTRE_USERNAME"
```

Remplacez `VOTRE_USERNAME` par votre vrai nom d'utilisateur PythonAnywhere.

**Exemple :** Si votre username est `johndoe`, changez en :
```python
username = "johndoe"
```

Sauvegardez avec `Ctrl + X`, puis `Y`, puis `Entrée`.

### Étape 5 : Créer l'application web

#### 5.1 Aller dans l'onglet Web
1. Cliquez sur l'onglet **"Web"** en haut du dashboard
2. Cliquez sur **"Add a new web app"**

#### 5.2 Configuration de l'app
1. **Domain name** : Gardez celui proposé (`votreusername.pythonanywhere.com`)
2. **Web framework** : Sélectionnez **"Manual configuration"**
3. **Python version** : Choisissez **"Python 3.10"**
4. Cliquez **"Next"**

#### 5.3 Configuration du code source
Dans la section **"Code"** de votre app web :

1. **Source code** : Laissez `/home/votreusername/` (par défaut)
2. **Working directory** : Changez pour `/home/votreusername/mlflow_project`

#### 5.4 Configuration du fichier WSGI
1. Trouvez la section **"Code"**
2. Cliquez sur le lien de votre fichier WSGI (quelque chose comme `/var/www/votreusername_pythonanywhere_com_wsgi.py`)
3. **Supprimez tout le contenu existant**
4. **Copiez-collez** le contenu de votre fichier `~/mlflow_project/wsgi.py`
5. **Sauvegardez** le fichier

### Étape 6 : Lancer votre serveur

#### 6.1 Recharger l'application
1. Retournez dans l'onglet **"Web"**
2. Cliquez sur le gros bouton vert **"Reload votreusername.pythonanywhere.com"**
3. Attendez que le reload se termine (jusqu'à 20 secondes)

#### 6.2 Tester votre serveur
1. Cliquez sur le lien de votre site : `https://votreusername.pythonanywhere.com`
2. **🎉 Vous devriez voir l'interface MLflow !**

**Si ça marche :** Félicitations ! Votre serveur MLflow est en ligne ! 🎉

**Si vous voyez une erreur :** Pas de panique, consultez la section [Dépannage](#-dépannage) plus bas.

### Étape 7 : Tester avec des données

#### 7.1 Télécharger le script de test
Retournez dans votre console Bash :
```bash
cd ~/mlflow_project
wget https://raw.githubusercontent.com/votre-repo/main/test.py
```

#### 7.2 Modifier le script (si nécessaire)
```bash
nano test.py
```
Vérifiez que le nom d'utilisateur est correct (normalement il se détecte automatiquement).

#### 7.3 Lancer le test
```bash
python3.10 test.py
```

**Résultat attendu :**
```
🧪 Test du serveur MLflow sur PythonAnywhere
==================================================
📍 Tracking URI: file:///home/votreusername/mlflow_project/mlruns
✅ Expérience 'test_deployment' créée
✅ Données d'exemple générées
🚀 Run démarré: abc123...
📊 Métriques loggées - R2 Score: 0.8234
🤖 Modèle sauvegardé

🎉 Test terminé avec succès!
🌐 Visitez votre serveur: https://votreusername.pythonanywhere.com
📁 Vous devriez voir l'expérience 'test_deployment' avec votre run
```

#### 7.4 Vérifier dans l'interface web
1. Retournez sur `https://votreusername.pythonanywhere.com`
2. Cliquez sur **"test_deployment"**
3. Vous devriez voir votre expérience avec les métriques ! 🎊

---

## 🎯 Utilisation de votre serveur MLflow

### Depuis votre ordinateur local

#### Installation locale
```bash
pip install mlflow
```

#### Connexion à votre serveur
```python
import mlflow

# Se connecter à votre serveur distant
mlflow.set_tracking_uri("https://votreusername.pythonanywhere.com")

# Créer une expérience
mlflow.set_experiment("mon_projet_ia")

# Logger vos résultats
with mlflow.start_run():
    # Vos métriques
    mlflow.log_metric("accuracy", 0.92)
    mlflow.log_metric("precision", 0.89)
    
    # Vos paramètres
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("batch_size", 32)
    
    # Des fichiers (images, graphiques, etc.)
    mlflow.log_artifact("mon_graphique.png")

print("✅ Expérience sauvegardée sur votre serveur !")
```

### Depuis PythonAnywhere (serveur)

```python
import mlflow
import os

# Configuration pour utilisation locale sur le serveur
username = "votreusername"  # Votre username
mlflow.set_tracking_uri(f"file:///home/{username}/mlflow_project/mlruns")

# Utilisation normale
with mlflow.start_run():
    mlflow.log_metric("server_metric", 0.95)
```

### Exemples concrets d'usage

#### Exemple 1 : Suivi d'entraînement scikit-learn
```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Connexion au serveur
mlflow.set_tracking_uri("https://votreusername.pythonanywhere.com")
mlflow.set_experiment("iris_classification")

# Données
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)

with mlflow.start_run():
    # Paramètres
    n_estimators = 100
    max_depth = 5
    
    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    
    # Entraînement
    clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
    clf.fit(X_train, y_train)
    
    # Évaluation
    accuracy = accuracy_score(y_test, clf.predict(X_test))
    mlflow.log_metric("accuracy", accuracy)
    
    # Sauvegarder le modèle
    mlflow.sklearn.log_model(clf, "random_forest_model")
    
    print(f"🎯 Modèle entraîné avec une précision de {accuracy:.2%}")
```

#### Exemple 2 : Comparaison de modèles
```python
import mlflow
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC

mlflow.set_tracking_uri("https://votreusername.pythonanywhere.com")
mlflow.set_experiment("model_comparison")

models = {
    "logistic_regression": LogisticRegression(),
    "random_forest": RandomForestClassifier(),
    "svm": SVC()
}

for name, model in models.items():
    with mlflow.start_run(run_name=name):
        model.fit(X_train, y_train)
        accuracy = accuracy_score(y_test, model.predict(X_test))
        
        mlflow.log_param("model_type", name)
        mlflow.log_metric("accuracy", accuracy)
        mlflow.sklearn.log_model(model, "model")
        
        print(f"{name}: {accuracy:.2%}")
```

---

## 🔧 Dépannage

### Erreurs courantes et solutions

#### ❌ "Internal Server Error" dans le navigateur

**Causes possibles :**
1. Vous n'avez pas changé `VOTRE_USERNAME` dans le fichier WSGI
2. MLflow n'est pas correctement installé
3. Erreur de syntaxe dans le fichier WSGI

**Solutions :**
1. **Vérifiez votre fichier WSGI :**
   ```bash
   nano ~/mlflow_project/wsgi.py
   ```
   Assurez-vous que `username = "votre_vrai_username"`

2. **Consultez les logs d'erreur :**
   - Onglet **Web** → section **"Log files"** → **"Error log"**
   - Regardez les dernières lignes pour voir l'erreur exacte

3. **Réinstaller MLflow :**
   ```bash
   pip3.10 uninstall mlflow
   pip3.10 install --user mlflow
   ```

#### ❌ "mlflow: command not found"

**Solution :**
```bash
# Redémarrer votre console ou utiliser le chemin complet
~/.local/bin/mlflow --version

# Ou ajouter au PATH
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

#### ❌ "Permission denied" ou erreurs de fichiers

**Solution :**
```bash
# Corriger les permissions
chmod -R 755 ~/mlflow_project
find ~/mlflow_project -type f -exec chmod 644 {} \;
find ~/mlflow_project -type d -exec chmod 755 {} \;
```

#### ❌ La page web affiche du code Python au lieu de l'interface

**Cause :** Configuration WSGI incorrecte

**Solution :**
1. Vérifiez que vous avez bien copié le contenu dans le **fichier WSGI de PythonAnywhere** (pas juste créé un fichier local)
2. Le fichier doit être dans `/var/www/votreusername_pythonanywhere_com_wsgi.py`

#### ❌ "No module named 'mlflow'"

**Solutions :**
```bash
# Option 1: Réinstaller
pip3.10 install --user mlflow

# Option 2: Vérifier l'installation
pip3.10 show mlflow

# Option 3: Utiliser pip3 au lieu de pip3.10
pip3 install --user mlflow
```

### Commandes de diagnostic

#### Vérifier l'installation complète
```bash
# Dans votre console PythonAnywhere
cd ~/mlflow_project

echo "=== Diagnostic MLflow ==="
echo "Python version:"
python3 --version

echo "MLflow version:"
mlflow --version

echo "Structure des fichiers:"
ls -la

echo "Contenu mlruns:"
ls -la mlruns/

echo "Permissions:"
ls -la ~/mlflow_project

echo "Variables d'environnement:"
echo $USER
```

#### Logs en temps réel
```bash
# Suivre les logs d'erreur en temps réel
tail -f /var/log/votreusername.pythonanywhere.com.error.log

# Suivre les logs d'accès
tail -f /var/log/votreusername.pythonanywhere.com.access.log
```

### Tests manuels

#### Test 1 : Vérifier que MLflow démarre localement
```bash
cd ~/mlflow_project
mlflow server --host 0.0.0.0 --port 5000 --backend-store-uri file:///home/$USER/mlflow_project/mlruns
```
Si ça fonctionne, le problème est dans la configuration web.

#### Test 2 : Vérifier les imports Python
```bash
python3 -c "import mlflow; print('MLflow OK')"
python3 -c "import mlflow.server; print('MLflow server OK')"
```

---

## 🚀 Fonctionnalités avancées

### Configuration avec base de données MySQL (comptes payants)

Si vous avez un compte payant PythonAnywhere, vous pouvez utiliser MySQL :

```python
# Dans votre wsgi.py
os.environ['MLFLOW_BACKEND_STORE_URI'] = 'mysql://username:password@hostname/database'
```

### Stockage d'artefacts externe (S3, Google Cloud)

```python
# Configuration S3
os.environ['MLFLOW_DEFAULT_ARTIFACT_ROOT'] = 's3://your-bucket/mlflow-artifacts'

# Configuration Google Cloud
os.environ['MLFLOW_DEFAULT_ARTIFACT_ROOT'] = 'gs://your-bucket/mlflow-artifacts'
```

### Authentification basique

```python
# Dans votre wsgi.py, ajouter :
os.environ['MLFLOW_TRACKING_USERNAME'] = 'your_username'
os.environ['MLFLOW_TRACKING_PASSWORD'] = 'your_password'
```

---

## 📚 Ressources supplémentaires

### Documentation officielle
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [PythonAnywhere Help](https://help.pythonanywhere.com/)
- [MLflow Tracking](https://mlflow.org/docs/latest/tracking.html)

### Tutoriels complémentaires
- [MLflow pour débutants](https://mlflow.org/docs/latest/tutorials-and-examples/tutorial.html)
- [Meilleures pratiques MLflow](https://mlflow.org/docs/latest/tracking.html#organizing-runs-in-experiments)

### Communauté
- [MLflow GitHub](https://github.com/mlflow/mlflow)
- [MLflow Slack](https://mlflow-users.slack.com/)

---

## 🤝 Support et contribution

### Besoin d'aide ?
1. **Vérifiez d'abord la section [Dépannage](#-dépannage)**
2. **Consultez les logs** dans PythonAnywhere
3. **Ouvrez une issue** sur ce repository avec :
   - Votre message d'erreur exact
   - Les étapes que vous avez suivies
   - Votre configuration (type de compte PA, etc.)

### Contribuer
Les contributions sont bienvenues ! 
- Améliorations du guide
- Correction de bugs dans les scripts
- Nouveaux exemples d'usage

---

## 🎉 Félicitations !

Si vous êtes arrivé jusqu'ici et que tout fonctionne, vous avez maintenant :

✅ **Un serveur MLflow personnel** accessible 24h/24  
✅ **Une URL publique** pour partager vos expériences  
✅ **Un stockage permanent** de vos modèles et métriques  
✅ **Une interface graphique** pour analyser vos résultats  
✅ **La possibilité de collaborer** avec votre équipe  

**Votre serveur MLflow est maintenant prêt à accompagner tous vos projets de machine learning !** 🚀

---
