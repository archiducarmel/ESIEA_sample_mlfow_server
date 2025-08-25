#!/usr/bin/env python3
"""
run_mlflow.py - Lanceur MLflow simple pour PythonAnywhere
"""

import os
import mlflow
from mlflow.server import get_app
import logging

# Configuration
HOST = "0.0.0.0"
PORT = 5000

def setup_mlflow():
    """Configure MLflow"""
    # Dossier courant
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Base de données SQLite
    db_path = os.path.join(current_dir, "mlflow.db")
    backend_store_uri = f"sqlite:///{db_path}"
    
    # Dossier des artefacts
    artifacts_path = os.path.join(current_dir, "artifacts")
    if not os.path.exists(artifacts_path):
        os.makedirs(artifacts_path)
    
    print(f"📊 Base de données: {backend_store_uri}")
    print(f"📁 Artefacts: {artifacts_path}")
    
    return backend_store_uri, artifacts_path

def create_sample_experiment():
    """Crée une expérience d'exemple si aucune n'existe"""
    try:
        experiments = mlflow.search_experiments()
        if len(experiments) <= 1:  # Seulement l'expérience par défaut
            print("🧪 Création d'une expérience d'exemple...")
            mlflow.create_experiment("Demo", tags={"type": "demo"})
            
            # Ajout d'un run d'exemple
            with mlflow.start_run(experiment_id=mlflow.get_experiment_by_name("Demo").experiment_id):
                mlflow.log_param("model", "demo")
                mlflow.log_metric("accuracy", 0.85)
                print("✅ Run d'exemple créé")
    except Exception as e:
        print(f"⚠️ Erreur lors de la création de l'exemple: {e}")

def main():
    """Fonction principale"""
    print("🚀 Démarrage de MLflow UI")
    print("=" * 30)
    
    # Configuration
    backend_store_uri, artifacts_path = setup_mlflow()
    
    # Configuration MLflow
    os.environ["MLFLOW_BACKEND_STORE_URI"] = backend_store_uri
    os.environ["MLFLOW_DEFAULT_ARTIFACT_ROOT"] = artifacts_path
    
    # Configuration du tracking URI
    mlflow.set_tracking_uri(backend_store_uri)
    
    # Création d'un exemple si nécessaire
    create_sample_experiment()
    
    print(f"🌐 MLflow UI disponible sur http://localhost:{PORT}")
    print("📝 Logs:")
    
    try:
        # Lancement du serveur MLflow
        os.system(f"mlflow ui --backend-store-uri {backend_store_uri} --default-artifact-root {artifacts_path} --host {HOST} --port {PORT}")
    except KeyboardInterrupt:
        print("\n👋 Arrêt du serveur MLflow")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()