#!/bin/bash

# Script de Instalação Automática do Robô Web
# Para Kali Linux

echo "🤖 INSTALADOR DO ROBÔ WEB AUTOMÁTICO"
echo "=================================="

# Atualiza o sistema
echo "📦 Atualizando sistema..."
sudo apt update

# Instala Python3 e pip se não estiverem instalados
echo "🐍 Verificando Python3..."
if ! command -v python3 &> /dev/null; then
    echo "Instalando Python3..."
    sudo apt install -y python3 python3-pip
else
    echo "✅ Python3 já está instalado"
fi

# Instala Chrome/Chromium
echo "🌐 Instalando navegador Chrome/Chromium..."
sudo apt install -y google-chrome-stable chromium-browser chromium-driver

# Instala dependências Python
echo "📚 Instalando dependências Python..."
cd /app/backend
pip3 install requests

echo ""
echo "✅ INSTALAÇÃO COMPLETA!"
echo "=================================="
echo "Para executar o robô, use o comando:"
echo "    ./run.sh"
echo ""
echo "Para parar o robô, pressione Ctrl+C"
echo "=================================="