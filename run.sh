#!/bin/bash

# Script de Execução do Robô Web
# Para Kali Linux

echo "🤖 INICIANDO ROBÔ WEB AUTOMÁTICO"
echo "==============================="
echo "🎯 SITE: saude.grupoaronseg.com.br"
echo "⏰ TEMPO: 20 segundos por visita"
echo "⌨️  SIMULA: Digitar URL no navegador"
echo "==============================="
echo "Pressione Ctrl+C para parar o robô"
echo "==============================="

# Vai para o diretório do projeto
cd /app

# Executa o robô
python3 robot_simple.py