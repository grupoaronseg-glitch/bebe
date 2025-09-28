# 🤖 Robô de Navegação Web Automática

## 📝 Descrição
Este robô automatiza a navegação entre dois sites específicos:
- `saude.grupoaronseg.com.br` (10 segundos)
- `grupoaronseg.com.br` (10 segundos)

O robô executa em modo **headless** (sem interface gráfica) e roda em **loop infinito** até ser interrompido.

## 🖥️ Compatibilidade
- **SO**: Kali Linux
- **Python**: 3.6+
- **Navegador**: Chrome/Chromium (instalado automaticamente)

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
- **Modo Headless**: Execução sem interface gráfica
- **Loop Infinito**: Executa até ser interrompido
- **Logs Detalhados**: Mostra todas as ações no terminal
- **Tratamento de Erros**: Recupera de falhas automaticamente
- **Parada Graceful**: Para corretamente com Ctrl+C
- **Instalação Automática**: Instala todas as dependências

### 📈 Logs Exibidos
- Início e fim de cada ciclo
- Carregamento de páginas
- Contagem regressiva (10 segundos por site)
- Título das páginas acessadas
- Tempo de carregamento
- Contador de ciclos executados
- Tratamento de erros

### 🔄 Fluxo de Execução
1. **Acessa** `saude.grupoaronseg.com.br`
2. **Permanece** 10 segundos
3. **Acessa** `grupoaronseg.com.br`
4. **Permanece** 10 segundos
5. **Repete** o ciclo indefinidamente

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
- `robot.py` - Script principal do robô
- `install.sh` - Instalação automática
- `run.sh` - Execução do robô
- `README_ROBOT.md` - Esta documentação

## 🔧 Exemplo de Saída
```
2024-01-15 10:30:01 - [ROBÔ] - INFO - 🤖 INICIANDO ROBÔ DE NAVEGAÇÃO WEB
2024-01-15 10:30:01 - [ROBÔ] - INFO - 🔄 INICIANDO CICLO #1
2024-01-15 10:30:01 - [ROBÔ] - INFO - 🌐 ACESSANDO: https://saude.grupoaronseg.com.br
2024-01-15 10:30:03 - [ROBÔ] - INFO - ✅ SUCESSO! Página carregada em 2.34 segundos
2024-01-15 10:30:03 - [ROBÔ] - INFO - ⏰ Permanecendo no site... 10 segundos restantes
...
2024-01-15 10:30:13 - [ROBÔ] - INFO - ✅ TEMPO COMPLETADO - Saindo do site
```

---
**Desenvolvido para automação web em Kali Linux** 🐉