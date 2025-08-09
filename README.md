# 🚨 Web Cache Poisoning Scanner

Uma ferramenta de reconhecimento de vulnerabilidades para detectar envenenamento de cache em aplicações web através da análise de cabeçalhos de resposta HTTP.

## 📋 Descrição

O **Web Cache Poisoning Scanner** é uma ferramenta de segurança desenvolvida em Python para identificar possíveis vulnerabilidades de envenenamento de cache em aplicações web. A ferramenta analisa cabeçalhos de resposta HTTP, especificamente o cabeçalho `X-Cache`, para detectar quando uma resposta está sendo servida a partir do cache.

## ⚠️ Aviso Legal

**ATENÇÃO**: Esta ferramenta é destinada APENAS para fins educacionais e de teste de segurança autorizado. O uso desta ferramenta em sistemas sem autorização explícita é ilegal e pode resultar em consequências legais. Sempre obtenha permissão antes de testar qualquer sistema.

## 🎯 Funcionalidades

- ✅ **Scanner de URL única**: Testa uma URL específica para vulnerabilidades de cache
- ✅ **Scanner em lote**: Processa múltiplas URLs de um arquivo de texto
- ✅ **Processamento paralelo**: Utiliza threads para acelerar o processo de escaneamento
- ✅ **Detecção inteligente**: Identifica cabeçalhos `X-Cache: hit` e variações
- ✅ **Barra de progresso**: Interface visual com tqdm para acompanhar o progresso
- ✅ **Relatório detalhado**: Exibe resultados organizados e claros

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

### Scanner de URL Única
```bash
python cache_poison_scanner.py -u "https://exemplo.com"
```

### Scanner em Lote
```bash
python cache_poison_scanner.py -l urls.txt -t 20
```

### Parâmetros Disponíveis

| Parâmetro | Descrição | Exemplo |
|-----------|-----------|---------|
| `-u, --url` | URL única para testar | `-u "https://site.com"` |
| `-l, --list` | Arquivo com lista de URLs | `-l urls.txt` |
| `-t, --threads` | Número de threads (padrão: 10) | `-t 20` |

## 📁 Formato do Arquivo de URLs

Crie um arquivo de texto (`urls.txt`) com uma URL por linha:

```txt
https://exemplo1.com
https://exemplo2.com
https://exemplo3.com
```

## 🔍 Como Funciona

1. **Preparação**: A ferramenta adiciona o parâmetro `?cache_poison=1` à URL de destino
2. **Teste inicial**: Faz uma requisição inicial para "aquecer" o cache
3. **Verificação**: Executa múltiplas requisições e analisa os cabeçalhos de resposta
4. **Detecção**: Identifica cabeçalhos `X-Cache: hit` ou variações similares
5. **Relatório**: Exibe URLs vulneráveis encontradas

## 📊 Exemplo de Saída

```
[*] Checking single URL: https://exemplo.com
[+] Cache Hit Detected: https://exemplo.com
```

Para múltiplas URLs:
```
Scanning URLs: 100%|██████████| 50/50 [00:30<00:00,  1.67url/s]

--------------------------------------------------
✅ Cache Hit Detected on the following URLs:
--------------------------------------------------
  -> https://vulneravel1.com
  -> https://vulneravel2.com
```

## 🚀 Recursos Avançados

- **Processamento paralelo**: Acelera o escaneamento com múltiplas threads
- **Tratamento de erros**: Gerencia timeouts e falhas de conexão graciosamente
- **Verificação SSL**: Suporta certificados auto-assinados (para testes internos)
- **Interface progressiva**: Barra de progresso em tempo real

## 🔧 Personalização

### Modificar Parâmetros de Cache
```python
POISON_PARAM = "?cache_poison=1"  # Altere o parâmetro de teste
CACHE_HIT_VALUES = {'hit', 'h'}   # Adicione novos valores de cache hit
```

### Ajustar Timeouts
```python
session.get(target_url, verify=False, timeout=10)  # Modifique o timeout
```

## 📚 Casos de Uso

- **Testes de penetração autorizados**
- **Auditorias de segurança web**
- **Pesquisa em segurança da informação**
- **Testes de infraestrutura de cache**

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

## 🔒 Segurança

- Desabilita avisos SSL para testes internos
- Timeout configurável para evitar travamentos
- Tratamento robusto de exceções de rede

## 📞 Suporte

Se você encontrar problemas ou tiver sugestões:

- Abra uma [Issue](../../issues) no GitHub
- Entre em contato: https://www.linkedin.com/in/gabriel-miranda-1b9961203/

## 🙏 Agradecimentos

- Comunidade de segurança da informação
- Contribuidores do projeto
- Ferramentas open source que inspiraram este projeto

---

**⚠️ Lembre-se**: Use esta ferramenta de forma responsável e sempre com autorização prévia! 
