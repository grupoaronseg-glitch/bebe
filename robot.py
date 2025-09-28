#!/usr/bin/env python3
"""
Robô de Navegação Web Automática
Desenvolvido para Kali Linux

Funcionalidades:
- Navega automaticamente entre dois sites
- saude.grupoaronseg.com.br (10 segundos)
- grupoaronseg.com.br (10 segundos)
- Loop infinito até interrupção (Ctrl+C)
- Execução headless (sem interface gráfica)
- Logs detalhados no terminal
"""

import time
import logging
import signal
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import subprocess
import os

class WebRobot:
    def __init__(self):
        self.driver = None
        self.sites = [
            "https://saude.grupoaronseg.com.br",
            "https://grupoaronseg.com.br"
        ]
        self.current_site = 0
        self.cycle_count = 0
        self.setup_logging()
        self.setup_signal_handler()

    def setup_logging(self):
        """Configura o sistema de logs"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - [ROBÔ] - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger(__name__)

    def setup_signal_handler(self):
        """Configura handler para interrupção graceful com Ctrl+C"""
        signal.signal(signal.SIGINT, self.signal_handler)

    def signal_handler(self, sig, frame):
        """Handler para parada graceful"""
        self.logger.info("🛑 INTERRUPÇÃO RECEBIDA - Parando robô...")
        self.logger.info(f"📊 TOTAL DE CICLOS EXECUTADOS: {self.cycle_count}")
        if self.driver:
            self.driver.quit()
            self.logger.info("✅ NAVEGADOR FECHADO COM SUCESSO")
        sys.exit(0)

    def setup_driver(self):
        """Configura o driver do Chrome em modo headless"""
        try:
            # Verifica se chromedriver está disponível
            result = subprocess.run(['which', 'chromedriver'], capture_output=True, text=True)
            if not result.stdout.strip():
                # Tenta instalar chromedriver automaticamente
                self.logger.warning("⚠️  ChromeDriver não encontrado. Tentando instalar...")
                self.install_chromedriver()

            chrome_options = Options()
            chrome_options.add_argument("--headless")  # Modo sem interface gráfica
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
            
            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.set_page_load_timeout(30)
            self.logger.info("✅ NAVEGADOR CONFIGURADO COM SUCESSO (Modo Headless)")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ ERRO AO CONFIGURAR NAVEGADOR: {e}")
            return False

    def install_chromedriver(self):
        """Instala chromedriver automaticamente"""
        try:
            # Instala chrome se não existir
            subprocess.run(['sudo', 'apt', 'update'], check=True, capture_output=True)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'google-chrome-stable'], check=True, capture_output=True)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'chromium-driver'], check=True, capture_output=True)
            self.logger.info("✅ ChromeDriver instalado com sucesso")
        except subprocess.CalledProcessError as e:
            self.logger.error(f"❌ Erro ao instalar ChromeDriver: {e}")

    def visit_site(self, url):
        """Visita um site e permanece por 10 segundos"""
        try:
            self.logger.info(f"🌐 ACESSANDO: {url}")
            start_time = time.time()
            
            self.driver.get(url)
            
            # Aguarda página carregar
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            
            load_time = time.time() - start_time
            self.logger.info(f"✅ SUCESSO! Página carregada em {load_time:.2f} segundos")
            self.logger.info(f"📄 TÍTULO DA PÁGINA: {self.driver.title}")
            
            # Permanece no site por 10 segundos
            for i in range(10, 0, -1):
                self.logger.info(f"⏰ Permanecendo no site... {i} segundos restantes")
                time.sleep(1)
            
            self.logger.info("✅ TEMPO COMPLETADO - Saindo do site")
            return True
            
        except TimeoutException:
            self.logger.error(f"⏰ TIMEOUT: Site {url} demorou muito para carregar")
            return False
        except WebDriverException as e:
            self.logger.error(f"❌ ERRO DE NAVEGAÇÃO: {e}")
            return False
        except Exception as e:
            self.logger.error(f"❌ ERRO INESPERADO: {e}")
            return False

    def run_cycle(self):
        """Executa um ciclo completo (ambos os sites)"""
        self.cycle_count += 1
        self.logger.info(f"🔄 INICIANDO CICLO #{self.cycle_count}")
        
        success = True
        for i, site in enumerate(self.sites, 1):
            self.logger.info(f"📍 SITE {i}/2 DO CICLO #{self.cycle_count}")
            if not self.visit_site(site):
                success = False
        
        if success:
            self.logger.info(f"✅ CICLO #{self.cycle_count} COMPLETADO COM SUCESSO!")
        else:
            self.logger.warning(f"⚠️  CICLO #{self.cycle_count} completado com erros")
        
        self.logger.info("⏸️  Pausa de 2 segundos antes do próximo ciclo...")
        time.sleep(2)

    def run(self):
        """Executa o robô em loop infinito"""
        self.logger.info("🤖 INICIANDO ROBÔ DE NAVEGAÇÃO WEB")
        self.logger.info("=" * 50)
        self.logger.info("🎯 SITES ALVO:")
        for i, site in enumerate(self.sites, 1):
            self.logger.info(f"   {i}. {site}")
        self.logger.info("⏱️  TEMPO POR SITE: 10 segundos")
        self.logger.info("🔁 MODO: Loop infinito (Ctrl+C para parar)")
        self.logger.info("=" * 50)

        if not self.setup_driver():
            self.logger.error("❌ Não foi possível configurar o navegador. Saindo...")
            return

        try:
            while True:
                self.run_cycle()
                
        except KeyboardInterrupt:
            self.logger.info("🛑 INTERRUPÇÃO MANUAL RECEBIDA")
        except Exception as e:
            self.logger.error(f"❌ ERRO CRÍTICO: {e}")
        finally:
            if self.driver:
                self.driver.quit()
                self.logger.info("✅ NAVEGADOR FECHADO")
            self.logger.info(f"📊 ROBÔ FINALIZADO - Total de ciclos: {self.cycle_count}")

def main():
    """Função principal"""
    robot = WebRobot()
    robot.run()

if __name__ == "__main__":
    main()