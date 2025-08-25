#!/usr/bin/env python3
"""
test_mlflow_simple.py - Test rapide de MLflow
"""

import mlflow
import os
from datetime import datetime

def test_mlflow():
    """Test simple de MLflow"""
    print("🧪 Test de MLflow")
    print("=" * 20)
    
    # Configuration du tracking URI
    current_dir = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(current_dir, "mlflow.db")
    mlflow.set_tracking_uri(f"sqlite:///{db_path}")
    
    # Création d'une expérience de test
    experiment_name = f"test-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
    
    try:
        exp_id = mlflow.create_experiment(experiment_name)
        print(f"✅ Expérience créée: {experiment_name}")
        
        # Lancement d'un run de test
        with mlflow.start_run(experiment_id=exp_id):
            # Log de paramètres
            mlflow.log_param("algorithm", "test")
            mlflow.log_param("dataset", "synthetic")
            
            # Log de métriques
            mlflow.log_metric("accuracy", 0.95)
            mlflow.log_metric("loss", 0.05)
            
            # Log d'un fichier
            with open("test_output.txt", "w") as f:
                f.write("Test MLflow réussi !")
            mlflow.log_artifact("test_output.txt")
            
            print("✅ Run de test terminé")
            
        print(f"🎉 Test réussi ! Vérifiez l'expérience '{experiment_name}' dans l'UI")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    test_mlflow()