#!/usr/bin/env python3
"""
Robô de Navegação Web Automática - Versão Simplificada
Desenvolvido para Kali Linux (ARM64/x86_64)

Funcionalidades:
- Faz requisições HTTP para os sites (simulando navegação)
- saude.grupoaronseg.com.br (10 segundos)
- grupoaronseg.com.br (10 segundos)
- Loop infinito até interrupção (Ctrl+C)
- Logs detalhados no terminal
- Compatível com qualquer arquitetura
"""

import time
import logging
import signal
import sys
import requests
from datetime import datetime
from urllib.parse import urljoin

class WebRobotSimple:
    def __init__(self):
        self.site = "https://saude.grupoaronseg.com.br"
        self.cycle_count = 0
        self.session = None
        self.setup_logging()
        self.setup_signal_handler()
        self.setup_session()

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
        if self.session:
            self.session.close()
            self.logger.info("✅ SESSÃO HTTP FECHADA COM SUCESSO")
        sys.exit(0)

    def setup_session(self):
        """Configura sessão HTTP com headers realistas"""
        try:
            self.session = requests.Session()
            self.session.headers.update({
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'pt-BR,pt;q=0.9,en;q=0.8',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1'
            })
            self.session.timeout = 30
            self.logger.info("✅ SESSÃO HTTP CONFIGURADA COM SUCESSO")
            return True
            
        except Exception as e:
            self.logger.error(f"❌ ERRO AO CONFIGURAR SESSÃO HTTP: {e}")
            return False

    def visit_site(self, url):
        """Visita um site fazendo requisição HTTP e permanece por 20 segundos"""
        try:
            self.logger.info(f"⌨️  DIGITANDO URL NO NAVEGADOR: {url}")
            time.sleep(1)  # Simula digitação
            
            self.logger.info(f"🌐 PRESSIONANDO ENTER - ACESSANDO: {url}")
            start_time = time.time()
            
            # Faz a requisição HTTP
            response = self.session.get(url)
            
            load_time = time.time() - start_time
            
            if response.status_code == 200:
                self.logger.info(f"✅ SUCESSO! Site carregado em {load_time:.2f} segundos")
                self.logger.info(f"📄 STATUS CODE: {response.status_code}")
                self.logger.info(f"📏 TAMANHO DA PÁGINA: {len(response.content)} bytes")
                
                # Extrai título da página se possível
                try:
                    if '<title>' in response.text and '</title>' in response.text:
                        title_start = response.text.find('<title>') + 7
                        title_end = response.text.find('</title>', title_start)
                        title = response.text[title_start:title_end].strip()
                        self.logger.info(f"📄 TÍTULO DA PÁGINA: {title[:100]}...")
                    else:
                        self.logger.info("📄 TÍTULO: Não encontrado no HTML")
                except:
                    self.logger.info("📄 TÍTULO: Erro ao extrair")
                
            else:
                self.logger.warning(f"⚠️  RESPOSTA NÃO-OK: Status {response.status_code}")
            
            # Permanece "navegando" por 20 segundos
            self.logger.info("⏰ PERMANECENDO NO SITE POR 20 SEGUNDOS...")
            for i in range(20, 0, -1):
                self.logger.info(f"⏰ {i} segundos restantes...")
                time.sleep(1)
            
            self.logger.info("✅ TEMPO COMPLETADO - 20 segundos no site")
            return True
            
        except requests.exceptions.Timeout:
            self.logger.error(f"⏰ TIMEOUT: Site {url} demorou mais que 30 segundos")
            return False
        except requests.exceptions.ConnectionError as e:
            self.logger.error(f"🌐 ERRO DE CONEXÃO: {e}")
            return False
        except requests.exceptions.RequestException as e:
            self.logger.error(f"❌ ERRO DE REQUISIÇÃO: {e}")
            return False
        except Exception as e:
            self.logger.error(f"❌ ERRO INESPERADO: {e}")
            return False

    def run_cycle(self):
        """Executa um ciclo completo (apenas um site)"""
        self.cycle_count += 1
        self.logger.info("=" * 60)
        self.logger.info(f"🔄 INICIANDO CICLO #{self.cycle_count}")
        self.logger.info("=" * 60)
        
        success = self.visit_site(self.site)
        
        if success:
            self.logger.info(f"✅ CICLO #{self.cycle_count} COMPLETADO COM SUCESSO!")
        else:
            self.logger.warning(f"⚠️  CICLO #{self.cycle_count} completado com erros")
        
        self.logger.info("⏸️  Pausa de 3 segundos antes do próximo ciclo...")
        time.sleep(3)

    def run(self):
        """Executa o robô em loop infinito"""
        self.logger.info("🤖 INICIANDO ROBÔ DE NAVEGAÇÃO WEB SIMPLIFICADO")
        self.logger.info("=" * 60)
        self.logger.info("🎯 SITES ALVO:")
        for i, site in enumerate(self.sites, 1):
            self.logger.info(f"   {i}. {site}")
        self.logger.info("⏱️  TEMPO POR SITE: 10 segundos")
        self.logger.info("🔁 MODO: Loop infinito (Ctrl+C para parar)")
        self.logger.info("🌐 MÉTODO: Requisições HTTP (compatível ARM64/x86_64)")
        self.logger.info("=" * 60)

        try:
            while True:
                self.run_cycle()
                
        except KeyboardInterrupt:
            self.logger.info("🛑 INTERRUPÇÃO MANUAL RECEBIDA")
        except Exception as e:
            self.logger.error(f"❌ ERRO CRÍTICO: {e}")
        finally:
            if self.session:
                self.session.close()
                self.logger.info("✅ SESSÃO HTTP FECHADA")
            self.logger.info(f"📊 ROBÔ FINALIZADO - Total de ciclos: {self.cycle_count}")

def main():
    """Função principal"""
    robot = WebRobotSimple()
    robot.run()

if __name__ == "__main__":
    main()