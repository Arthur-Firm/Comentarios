# 🤖 LinkedIn Auto-Engager

**LinkedIn Auto-Engager** é uma ferramenta de automação inteligente para o LinkedIn que utiliza IA e automação de navegador para:

- Interpretar publicações no LinkedIn e identificar se correspondem a descrições-alvo.
- Gerar comentários automáticos baseados no conteúdo analisado.
- Conectar-se automaticamente com pessoas de acordo com descrições desejadas.

---

## ✨ Funcionalidades

- 🔍 **Análise de Posts**: Interpreta o conteúdo de posts utilizando Gemini AI para verificar se estão relacionados à área de interesse configurada.
- 💬 **Geração de Comentários**: Produz comentários contextuais e relevantes para aumentar a interação no LinkedIn.
- 🤝 **Conexão com Perfis**: Procura usuários e envia solicitações de conexão com base em palavras-chave específicas.

---

## 🛠️ Tecnologias Utilizadas

- [Gemini API](https://deepmind.google/technologies/gemini/) (IA para interpretação e geração de texto)
- [Python](https://www.python.org/)
- [Selenium](https://www.selenium.dev/) (automação de navegador)
- [Chromedriver](https://chromedriver.chromium.org/) 

---

## ⚙️ Como Funciona

1. Faz login na conta do LinkedIn utilizando Selenium.
2. Acompanha o feed 
3. Para cada post encontrado:
   - Utiliza Gemini AI para analisar o conteúdo do post.
   - Verifica se ele está alinhado com a descrição-alvo.
   - Se aprovado, gera e publica um comentário automático.
4. Paralelamente, busca perfis relevantes e envia convites de conexão.

---

## 🚀 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/Arthur-Firm/linkedin_AutoEngager.git
cd linkedinAutoEngager
pip install -r requirements.txt
