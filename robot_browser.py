#!/usr/bin/env python3
"""
Robô de Navegação Web Automática - Com Navegador Real
Desenvolvido para Kali Linux

Funcionalidades:
- Abre navegador Firefox
- Acessa saude.grupoaronseg.com.br
- Permanece 20 segundos no site
- Fecha navegador
- Repete o ciclo infinitamente
- Loop infinito até interrupção (Ctrl+C)
"""

import time
import logging
import signal
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
import subprocess
import os

class WebRobotBrowser:
    def __init__(self):
        self.driver = None
        self.site = "https://saude.grupoaronseg.com.br"
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
            try:
                self.driver.quit()
                self.logger.info("✅ NAVEGADOR FECHADO COM SUCESSO")
            except:
                self.logger.warning("⚠️  Erro ao fechar navegador")
        sys.exit(0)

    def setup_driver(self):
        """Configura o driver do Firefox em modo headless"""
        try:
            # Primeiro tenta com webdriver-manager
            try:
                from webdriver_manager.firefox import GeckoDriverManager
                
                firefox_options = FirefoxOptions()
                firefox_options.add_argument("--headless")  # Modo sem interface gráfica
                firefox_options.add_argument("--width=1920")
                firefox_options.add_argument("--height=1080")
                
                service = Service(GeckoDriverManager().install())
                self.driver = webdriver.Firefox(service=service, options=firefox_options)
                self.driver.set_page_load_timeout(30)
                self.logger.info("✅ FIREFOX CONFIGURADO COM WEBDRIVER-MANAGER (Modo Headless)")
                return True
                
            except Exception as manager_error:
                self.logger.warning(f"⚠️  WebDriver Manager falhou: {manager_error}")
                
                # Fallback para geckodriver local
                try:
                    firefox_options = FirefoxOptions()
                    firefox_options.add_argument("--headless")
                    firefox_options.add_argument("--width=1920")
                    firefox_options.add_argument("--height=1080")
                    
                    self.driver = webdriver.Firefox(options=firefox_options)
                    self.driver.set_page_load_timeout(30)
                    self.logger.info("✅ FIREFOX CONFIGURADO COM GECKODRIVER LOCAL (Modo Headless)")
                    return True
                    
                except Exception as local_error:
                    self.logger.error(f"❌ Firefox local também falhou: {local_error}")
                    
                    # Último recurso: modo visível (não headless)
                    try:
                        self.driver = webdriver.Firefox()
                        self.driver.set_page_load_timeout(30)
                        self.logger.info("✅ FIREFOX CONFIGURADO EM MODO VISÍVEL")
                        return True
                        
                    except Exception as final_error:
                        self.logger.error(f"❌ Todas as tentativas falharam: {final_error}")
                        return False
            
        except Exception as e:
            self.logger.error(f"❌ ERRO CRÍTICO AO CONFIGURAR NAVEGADOR: {e}")
            return False

    def visit_site(self):
        """Visita o site e permanece por 20 segundos"""
        try:
            self.logger.info(f"🌐 DIGITANDO URL NO NAVEGADOR: {self.site}")
            start_time = time.time()
            
            # Navega para o site (simula digitar a URL)
            self.driver.get(self.site)
            
            # Aguarda página carregar
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            
            load_time = time.time() - start_time
            self.logger.info(f"✅ SUCESSO! Página carregada em {load_time:.2f} segundos")
            
            # Obtém informações da página
            try:
                title = self.driver.title
                current_url = self.driver.current_url
                self.logger.info(f"📄 TÍTULO DA PÁGINA: {title}")
                self.logger.info(f"🔗 URL ATUAL: {current_url}")
            except Exception as e:
                self.logger.warning(f"⚠️  Erro ao obter info da página: {e}")
            
            # Permanece no site por 20 segundos
            self.logger.info("⏰ PERMANECENDO NO SITE POR 20 SEGUNDOS...")
            for i in range(20, 0, -1):
                self.logger.info(f"⏰ {i} segundos restantes...")
                time.sleep(1)
            
            self.logger.info("✅ TEMPO COMPLETADO - 20 segundos no site")
            return True
            
        except TimeoutException:
            self.logger.error(f"⏰ TIMEOUT: Site {self.site} demorou muito para carregar")
            return False
        except WebDriverException as e:
            self.logger.error(f"❌ ERRO DE NAVEGAÇÃO: {e}")
            return False
        except Exception as e:
            self.logger.error(f"❌ ERRO INESPERADO: {e}")
            return False

    def close_browser(self):
        """Fecha o navegador completamente"""
        try:
            if self.driver:
                self.driver.quit()
                self.logger.info("✅ NAVEGADOR FECHADO")
                self.driver = None
                return True
        except Exception as e:
            self.logger.error(f"❌ ERRO AO FECHAR NAVEGADOR: {e}")
            return False

    def run_cycle(self):
        """Executa um ciclo completo"""
        self.cycle_count += 1
        self.logger.info("=" * 60)
        self.logger.info(f"🔄 INICIANDO CICLO #{self.cycle_count}")
        self.logger.info("=" * 60)
        
        # Abre navegador
        if not self.setup_driver():
            self.logger.error("❌ Não foi possível abrir o navegador")
            return False
        
        # Visita o site
        success = self.visit_site()
        
        # Fecha navegador
        self.close_browser()
        
        if success:
            self.logger.info(f"✅ CICLO #{self.cycle_count} COMPLETADO COM SUCESSO!")
        else:
            self.logger.warning(f"⚠️  CICLO #{self.cycle_count} completado com erros")
        
        self.logger.info("⏸️  Pausa de 3 segundos antes do próximo ciclo...")
        time.sleep(3)
        
        return success

    def run(self):
        """Executa o robô em loop infinito"""
        self.logger.info("🤖 ROBÔ DE NAVEGAÇÃO WEB COM NAVEGADOR REAL")
        self.logger.info("=" * 60)
        self.logger.info("🎯 SITE ALVO: saude.grupoaronseg.com.br")
        self.logger.info("⏱️  TEMPO NO SITE: 20 segundos")
        self.logger.info("🔁 MODO: Loop infinito (Ctrl+C para parar)")
        self.logger.info("🌐 NAVEGADOR: Firefox (abre e fecha a cada ciclo)")
        self.logger.info("=" * 60)

        try:
            while True:
                self.run_cycle()
                
        except KeyboardInterrupt:
            self.logger.info("🛑 INTERRUPÇÃO MANUAL RECEBIDA")
        except Exception as e:
            self.logger.error(f"❌ ERRO CRÍTICO: {e}")
        finally:
            self.close_browser()
            self.logger.info(f"📊 ROBÔ FINALIZADO - Total de ciclos: {self.cycle_count}")

def main():
    """Função principal"""
    robot = WebRobotBrowser()
    robot.run()

if __name__ == "__main__":
    main()