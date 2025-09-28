# 🤖 Robô de Navegação Web Automática

## 📝 Descrição
Este robô automatiza a navegação para o site específico:
- `saude.grupoaronseg.com.br` (permanece 20 segundos)

O robô simula **digitar a URL no navegador** e executa em **loop infinito** até ser interrompido.

## 🖥️ Compatibilidade
- **SO**: Kali Linux (ARM64/x86_64)
- **Python**: 3.6+
- **Método**: Requisições HTTP (não requer navegador)

## 🚀 Instalação e Execução

### Instalação Automática
```bash
# Dar permissão de execução
chmod +x install.sh run.sh

# Executar instalação
./install.sh
```

### Execução
```bash
# Executar o robô
./run.sh
```

### Parar o Robô
Pressione `Ctrl+C` no terminal para parar o robô gracefully.

## 📊 Funcionalidades

### ✅ Recursos Implementados
- **Requisições HTTP**: Execução via requests (sem dependência de navegador)
- **Loop Infinito**: Executa até ser interrompido
- **Logs Detalhados**: Mostra todas as ações no terminal
- **Tratamento de Erros**: Recupera de falhas automaticamente
- **Parada Graceful**: Para corretamente com Ctrl+C
- **Instalação Simples**: Apenas Python e requests
- **Multi-arquitetura**: Funciona em ARM64 e x86_64

### 📈 Logs Exibidos
- Início e fim de cada ciclo
- Simulação de digitação da URL
- Carregamento da página
- Status codes e tamanho das páginas
- Títulos das páginas (quando disponíveis)
- Contagem regressiva (20 segundos)
- Tempo de resposta do site
- Contador de ciclos executados
- Tratamento de erros de conexão

### 🔄 Fluxo de Execução
1. **Digita** `saude.grupoaronseg.com.br` no navegador
2. **Pressiona Enter** para acessar
3. **Permanece** 20 segundos no site
4. **Repete** o ciclo indefinidamente

## 🛠️ Configurações Técnicas

### Selenium WebDriver
- **Navegador**: Chrome em modo headless
- **Timeout**: 30 segundos para carregamento
- **User-Agent**: Linux Chrome
- **Resolução**: 1920x1080

### Logs
- **Formato**: Timestamp + Nível + Mensagem
- **Níveis**: INFO, WARNING, ERROR
- **Emojis**: Para fácil identificação visual

## 🚨 Solução de Problemas

### ChromeDriver não encontrado
O script instala automaticamente, mas se houver problemas:
```bash
sudo apt install chromium-driver
```

### Problemas de permissão
```bash
chmod +x install.sh run.sh
```

### Erro de dependências Python
```bash
pip3 install selenium webdriver-manager
```

## 📄 Arquivos do Projeto
- `robot_simple.py` - Script principal do robô (versão HTTP)
- `robot.py` - Script com Selenium (requer ChromeDriver)
- `install.sh` - Instalação automática
- `run.sh` - Execução do robô
- `README_ROBOT.md` - Esta documentação

## 🔧 Exemplo de Saída
```
2025-09-28 18:13:56 - [ROBÔ] - INFO - 🤖 INICIANDO ROBÔ DE NAVEGAÇÃO WEB SIMPLIFICADO
2025-09-28 18:13:56 - [ROBÔ] - INFO - 🔄 INICIANDO CICLO #1
2025-09-28 18:13:56 - [ROBÔ] - INFO - 🌐 ACESSANDO: https://saude.grupoaronseg.com.br
2025-09-28 18:13:58 - [ROBÔ] - INFO - ✅ SUCESSO! Site acessado em 1.87 segundos
2025-09-28 18:13:58 - [ROBÔ] - INFO - 📄 STATUS CODE: 200
2025-09-28 18:13:58 - [ROBÔ] - INFO - 📏 TAMANHO DA RESPOSTA: 138675 bytes
2025-09-28 18:13:58 - [ROBÔ] - INFO - 📄 TÍTULO DA PÁGINA: Método Secar em 20 Dias...
2025-09-28 18:13:58 - [ROBÔ] - INFO - ⏰ Permanecendo no site... 10 segundos restantes
...
```

---
**Desenvolvido para automação web em Kali Linux** 🐉