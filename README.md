# 🚨 Advanced Web Cache Poisoning Scanner & Exploit Tool

Uma ferramenta avançada de reconhecimento e exploração de vulnerabilidades de envenenamento de cache em aplicações web, com múltiplas técnicas de detecção e exploração automatizada.

## 📋 Descrição

O **Advanced Web Cache Poisoning Scanner** é uma ferramenta profissional de segurança desenvolvida em Python para identificar e explorar vulnerabilidades de envenenamento de cache em aplicações web. A ferramenta utiliza técnicas avançadas de detecção, incluindo análise de cabeçalhos HTTP, verificação de respostas em cache e múltiplas estratégias de exploração automatizada.

## ⚠️ Aviso Legal

**ATENÇÃO**: Esta ferramenta é destinada APENAS para fins educacionais e de teste de segurança autorizado. O uso desta ferramenta em sistemas sem autorização explícita é ilegal e pode resultar em consequências legais. Sempre obtenha permissão antes de testar qualquer sistema.

## 🎯 Funcionalidades Principais

### 🔍 **Detecção Avançada**
- ✅ **Scanner de URL única**: Testa uma URL específica para vulnerabilidades de cache
- ✅ **Scanner em lote**: Processa múltiplas URLs de um arquivo de texto
- ✅ **Processamento paralelo**: Utiliza threads para acelerar o processo de escaneamento
- ✅ **Detecção inteligente**: Identifica cabeçalhos `X-Cache: hit` e variações
- ✅ **Análise de respostas**: Verifica múltiplos indicadores de cache
- ✅ **Barra de progresso**: Interface visual com tqdm para acompanhar o progresso

### 🚀 **Sistema de Exploit Automatizado**
- ✅ **4 técnicas de exploração**: Header injection, parameter pollution, host manipulation, redirect manipulation
- ✅ **Payloads personalizáveis**: Suporte a payloads customizados
- ✅ **Cache busting inteligente**: Geração de parâmetros únicos para evitar cache
- ✅ **Verificação de sucesso**: Múltiplos métodos para confirmar exploits bem-sucedidos
- ✅ **Logging detalhado**: Sistema de logs com timestamps e níveis

### 📊 **Recursos Avançados**
- ✅ **Output em JSON**: Salva resultados em formato estruturado
- ✅ **Modo verbose**: Logging detalhado para debugging
- ✅ **Tratamento de erros robusto**: Gerencia timeouts e falhas graciosamente
- ✅ **Verificação SSL**: Suporte a certificados auto-assinados
- ✅ **Análise de metadados**: Informações detalhadas sobre vulnerabilidades detectadas

## 🛠️ Requisitos

- Python 3.6+
- Bibliotecas Python (instaladas via pip):
  - `requests`
  - `urllib3`
  - `tqdm`

## 📦 Instalação

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/web-cache-poisoning-scanner.git
cd web-cache-poisoning-scanner
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute a ferramenta:**
```bash
python cache_poison_scanner.py --help
```

## 📖 Como Usar

### 🔍 **Scanner Básico**
```bash
# URL única
python cache_poison_scanner.py -u "https://exemplo.com"

# Lista de URLs
python cache_poison_scanner.py -l urls.txt -t 20
```

### 🚀 **Modo Exploit**
```bash
# Com exploit automático
python cache_poison_scanner.py -l urls.txt -x

# Com payload customizado
python cache_poison_scanner.py -l urls.txt -x -p "https://meu-site-malicioso.com"

# Modo verbose com exploit
python cache_poison_scanner.py -l urls.txt -x -v
```

### 💾 **Salvando Resultados**
```bash
# Salvar resultados em JSON
python cache_poison_scanner.py -l urls.txt -x -o resultados.json
```

## 🎛️ Parâmetros Disponíveis

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-u, --url` | URL única para testar | `-u "https://site.com"` |
| `-l, --list` | Arquivo com lista de URLs | `-l urls.txt` |
| `-t, --threads` | Número de threads (padrão: 10) | `-t 20` |
| `-x, --exploit` | Executar exploits automáticos | `-x` |
| `-v, --verbose` | Modo verbose com logs detalhados | `-v` |
| `-p, --payload` | Payload customizado para exploits | `-p "https://evil.com"` |
| `-o, --output` | Arquivo de saída para resultados | `-o resultados.json` |

## 🔍 Como Funciona

### **1. Detecção de Vulnerabilidades**
1. **Preparação**: Adiciona parâmetros únicos para evitar cache
2. **Teste inicial**: Faz requisição inicial para "aquecer" o cache
3. **Verificação múltipla**: Executa várias requisições e analisa respostas
4. **Análise inteligente**: Verifica cabeçalhos, status codes e tamanhos de resposta
5. **Confirmação**: Identifica padrões que indicam cache poisoning

### **2. Sistema de Exploit**
1. **Header Injection**: Testa injeção de cabeçalhos maliciosos
2. **Parameter Pollution**: Manipula parâmetros de URL
3. **Host Manipulation**: Altera cabeçalhos de host
4. **Redirect Manipulation**: Explora redirecionamentos

## 📁 Formato do Arquivo de URLs

Crie um arquivo de texto (`urls.txt`) com uma URL por linha:

```txt
https://exemplo1.com
https://exemplo2.com
https://exemplo3.com
```

## 📊 Exemplo de Saída

### **Scanner Básico**
```
[*] 🔍 Checking single URL: https://exemplo.com
[+] 🎯 Cache Hit Detected: https://exemplo.com
    📊 Cache Info: {'cache_hit': True, 'cache_header': 'hit from cache'}
```

### **Scanner com Exploit**
```
🔍 Scanning URLs: 100%|██████████| 50/50 [00:30<00:00,  1.67url/s]

============================================================
🎯 CACHE POISONING VULNERABILITIES DETECTED!
============================================================
   1. https://vulneravel1.com
   2. https://vulneravel2.com
============================================================

[14:30:25] [EXPLOIT] 🚀 Starting cache poisoning exploit on 2 vulnerable URLs
[14:30:25] [EXPLOIT] 🎯 Targeting: https://vulneravel1.com
[14:30:26] [SUCCESS] 🎯 Header injection successful: x-forwarded-host = evil.com
```

## 🚀 Técnicas de Exploit

### **1. Header Injection**
- Injeção de cabeçalhos HTTP maliciosos
- Testa 30+ cabeçalhos diferentes
- Verifica reflexão de payloads

### **2. Parameter Pollution**
- Manipulação de parâmetros de URL
- Testa parâmetros de redirecionamento
- Verifica mudanças de comportamento

### **3. Host Header Manipulation**
- Alteração do cabeçalho Host
- Testa diferentes valores de host
- Verifica respostas alteradas

### **4. Redirect Manipulation**
- Exploração de redirecionamentos
- Manipula cabeçalhos de rewrite
- Verifica mudanças de destino

## 🔧 Personalização

### **Modificar Headers de Exploit**
```python
EXPLOIT_HEADERS = {
    "x-custom-header": "meu-payload",
    "x-malicious": "payload-personalizado"
}
```

### **Ajustar Configurações**
```python
TIMEOUT_DELAY = 15        # Timeout das requisições
MAX_RETRIES = 5           # Número de tentativas
CACHE_HIT_VALUES = {'hit', 'h', 'cached'}  # Valores de cache
```

## 📚 Casos de Uso

- **Testes de penetração autorizados**
- **Auditorias de segurança web**
- **Pesquisa em segurança da informação**
- **Testes de infraestrutura de cache**
- **Análise de vulnerabilidades em CDNs**
- **Testes de segurança em aplicações web**

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## ⚡ Performance

- **URL única**: ~2-5 segundos
- **100 URLs**: ~30-60 segundos (com 10 threads)
- **1000 URLs**: ~5-10 minutos (com 20 threads)
- **Modo exploit**: +2-5 segundos por URL vulnerável

## 🔒 Segurança e Recursos

- **Cache busting inteligente**: Evita falsos positivos
- **Timeout configurável**: Previne travamentos
- **Tratamento robusto de exceções**: Gerencia erros graciosamente
- **Verificação SSL flexível**: Suporta ambientes internos
- **Logging estruturado**: Facilita debugging e análise

## 📞 Suporte

Se você encontrar problemas ou tiver sugestões:

- Abra uma [Issue](../../issues) no GitHub
- Entre em contato: [seu-email@exemplo.com](mailto:seu-email@exemplo.com)

## 🙏 Agradecimentos

- Comunidade de segurança da informação
- Contribuidores do projeto
- Ferramentas open source que inspiraram este projeto
- Pesquisadores de cache poisoning

---

**⚠️ Lembre-se**: Use esta ferramenta de forma responsável e sempre com autorização prévia!

**🔬 Para pesquisadores**: Esta ferramenta implementa técnicas avançadas de cache poisoning e deve ser usada apenas em ambientes controlados e autorizados. 
