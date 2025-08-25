"""
Script de test pour vérifier que MLflow fonctionne sur PythonAnywhere
Usage: python3.10 test.py
"""

import mlflow
import mlflow.sklearn
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import os

def main():
    print("🧪 Test du serveur MLflow sur PythonAnywhere")
    print("=" * 50)
    
    # ⚠️ Remplacez par votre vrai nom d'utilisateur
    username = os.getenv('USER', 'VOTRE_USERNAME')
    
    if username == 'VOTRE_USERNAME':
        print("❌ ERREUR: Vous devez remplacer 'VOTRE_USERNAME' par votre vrai nom d'utilisateur")
        return
    
    # Configuration MLflow local
    tracking_uri = f"file:///home/{username}/mlflow_project/mlruns"
    mlflow.set_tracking_uri(tracking_uri)
    
    print(f"📍 Tracking URI: {tracking_uri}")
    
    try:
        # Créer une expérience de test
        mlflow.set_experiment("test_deployment")
        print("✅ Expérience 'test_deployment' créée")
        
        # Générer des données d'exemple
        X, y = make_regression(n_samples=100, n_features=1, noise=10, random_state=42)
        print("✅ Données d'exemple générées")
        
        # Démarrer un run MLflow
        with mlflow.start_run() as run:
            print(f"🚀 Run démarré: {run.info.run_id}")
            
            # Entraîner un modèle simple
            model = LinearRegression()
            model.fit(X, y)
            
            # Logger des métriques
            score = model.score(X, y)
            mlflow.log_metric("r2_score", score)
            mlflow.log_metric("test_metric", 0.95)
            
            # Logger des paramètres
            mlflow.log_param("n_samples", 100)
            mlflow.log_param("n_features", 1)
            mlflow.log_param("model_type", "LinearRegression")
            
            # Logger le modèle
            mlflow.sklearn.log_model(model, "linear_regression_model")
            
            print(f"📊 Métriques loggées - R2 Score: {score:.4f}")
            print(f"🤖 Modèle sauvegardé")
            
        print("\n🎉 Test terminé avec succès!")
        print(f"🌐 Visitez votre serveur: https://{username}.pythonanywhere.com")
        print("📁 Vous devriez voir l'expérience 'test_deployment' avec votre run")
        
    except Exception as e:
        print(f"❌ Erreur durant le test: {str(e)}")
        print("\n🔧 Solutions possibles:")
        print("1. Vérifiez que MLflow est installé: pip3.10 install --user mlflow")
        print("2. Vérifiez les permissions: chmod -R 755 ~/mlflow_project")
        print("3. Vérifiez que les dossiers existent: ls -la ~/mlflow_project")

if __name__ == "__main__":
    main()