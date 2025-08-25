import sys
import os

# ⚠️ IMPORTANT: Remplacez VOTRE_USERNAME par votre vrai nom d'utilisateur PythonAnywhere
username = "VOTRE_USERNAME"

# Ajouter les chemins nécessaires
sys.path.insert(0, f'/home/{username}/.local/lib/python3.10/site-packages')
sys.path.insert(0, f'/home/{username}/mlflow_project')

# Configuration MLflow
os.environ['MLFLOW_BACKEND_STORE_URI'] = f'file:///home/{username}/mlflow_project/mlruns'
os.environ['MLFLOW_DEFAULT_ARTIFACT_ROOT'] = f'/home/{username}/mlflow_project/artifacts'

# Importer et configurer MLflow
try:
    import mlflow.server
    from mlflow.server import app as application
    
    print(f"MLflow configuré avec succès pour {username}")
    
except ImportError as e:
    # Application de fallback
    from flask import Flask
    application = Flask(__name__)
    
    @application.route('/')
    def home():
        return f"""
        <h1>Erreur MLflow</h1>
        <p>Erreur: {str(e)}</p>
        <p>Vérifiez que MLflow est installé avec: <code>pip3.10 install --user mlflow</code></p>
        """

if __name__ == "__main__":
    application.run()