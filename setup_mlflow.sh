#!/bin/bash
# setup_mlflow.sh - Installation simple MLflow avec service systemd

echo "🚀 Installation MLflow avec service systemd"
echo "============================================"

# Variables
SERVICE_NAME="mlflow"
MLFLOW_DIR="$HOME/mlflow"
MLFLOW_USER=$(whoami)

# Installation de MLflow
echo "📦 Installation de MLflow..."
pip3 install --user mlflow

# Création du dossier de travail
echo "📁 Création du dossier de travail..."
mkdir -p $MLFLOW_DIR
cd $MLFLOW_DIR

# Création du dossier pour les artefacts
mkdir -p artifacts

# Fonction pour créer le service systemd
create_systemd_service() {
    echo "🔧 Création du service systemd..."
    
    # Détection du chemin Python
    PYTHON_PATH=$(which python3)
    MLFLOW_PATH=$(which mlflow)
    
    # Si mlflow n'est pas dans le PATH, chercher dans ~/.local/bin
    if [ -z "$MLFLOW_PATH" ]; then
        MLFLOW_PATH="$HOME/.local/bin/mlflow"
    fi
    
    # Création du fichier service
    sudo tee /etc/systemd/system/$SERVICE_NAME.service > /dev/null << EOF
[Unit]
Description=MLflow Tracking Server
After=network.target

[Service]
Type=exec
User=$MLFLOW_USER
Group=$MLFLOW_USER
WorkingDirectory=$MLFLOW_DIR
Environment=PATH=$HOME/.local/bin:/usr/local/bin:/usr/bin:/bin
ExecStart=$MLFLOW_PATH ui --backend-store-uri sqlite:///$MLFLOW_DIR/mlflow.db --default-artifact-root $MLFLOW_DIR/artifacts --host 0.0.0.0 --port 5000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
EOF

    echo "✅ Service systemd créé"
}

# Fonction pour gérer le service
manage_service() {
    # Vérifier si le service existe
    if systemctl list-unit-files | grep -q "^$SERVICE_NAME.service"; then
        echo "🔄 Service $SERVICE_NAME existe déjà, redémarrage..."
        sudo systemctl daemon-reload
        sudo systemctl restart $SERVICE_NAME
        sudo systemctl status $SERVICE_NAME --no-pager -l
    else
        echo "🆕 Création et activation du service $SERVICE_NAME..."
        create_systemd_service
        sudo systemctl daemon-reload
        sudo systemctl enable $SERVICE_NAME
        sudo systemctl start $SERVICE_NAME
        sudo systemctl status $SERVICE_NAME --no-pager -l
    fi
}

# Création d'un script de gestion simplifié
create_management_script() {
    echo "🛠️ Création du script de gestion..."
    
    cat > $MLFLOW_DIR/manage.sh << 'EOF'
#!/bin/bash
# Script de gestion MLflow

SERVICE_NAME="mlflow"

case "${1:-status}" in
    start)
        echo "🚀 Démarrage de MLflow..."
        sudo systemctl start $SERVICE_NAME
        ;;
    stop)
        echo "🛑 Arrêt de MLflow..."
        sudo systemctl stop $SERVICE_NAME
        ;;
    restart)
        echo "🔄 Redémarrage de MLflow..."
        sudo systemctl restart $SERVICE_NAME
        ;;
    status)
        echo "📊 État de MLflow:"
        sudo systemctl status $SERVICE_NAME --no-pager -l
        ;;
    logs)
        echo "📝 Logs de MLflow:"
        sudo journalctl -u $SERVICE_NAME -f
        ;;
    enable)
        echo "⚡ Activation au démarrage..."
        sudo systemctl enable $SERVICE_NAME
        ;;
    disable)
        echo "❌ Désactivation au démarrage..."
        sudo systemctl disable $SERVICE_NAME
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status|logs|enable|disable}"
        echo ""
        echo "Commandes disponibles:"
        echo "  start    - Démarrer MLflow"
        echo "  stop     - Arrêter MLflow"
        echo "  restart  - Redémarrer MLflow"
        echo "  status   - Voir l'état du service"
        echo "  logs     - Voir les logs en temps réel"
        echo "  enable   - Activer au démarrage"
        echo "  disable  - Désactiver au démarrage"
        ;;
esac
EOF

    chmod +x $MLFLOW_DIR/manage.sh
    echo "✅ Script de gestion créé : $MLFLOW_DIR/manage.sh"
}

# Vérification des permissions sudo
check_sudo() {
    if ! sudo -n true 2>/dev/null; then
        echo "⚠️ Ce script nécessite les permissions sudo pour gérer le service systemd"
        echo "Veuillez entrer votre mot de passe si demandé..."
    fi
}

# Exécution principale
main() {
    check_sudo
    manage_service
    create_management_script
    
    echo ""
    echo "✅ Installation terminée !"
    echo "========================="
    echo ""
    echo "MLflow est maintenant disponible en tant que service systemd !"
    echo ""
    echo "Commandes utiles :"
    echo "  $MLFLOW_DIR/manage.sh status    # Voir l'état"
    echo "  $MLFLOW_DIR/manage.sh logs      # Voir les logs"
    echo "  $MLFLOW_DIR/manage.sh restart   # Redémarrer"
    echo ""
    echo "Interface web disponible sur :"
    echo "  http://localhost:5000"
    echo "  http://$(hostname -I | awk '{print $1}'):5000"
    echo ""
    
    # Affichage de l'état final
    echo "📊 État actuel du service :"
    sudo systemctl status $SERVICE_NAME --no-pager -l
}

main
