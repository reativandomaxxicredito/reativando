# Reativando — Site estático (Vercel + GitHub)

Este repositório contém os arquivos do site **Reativando** (HTML/CSS/JS estático).  
Fluxo recomendado: **GitHub → Vercel (conta grátis)**. Depois, apontamos o subdomínio **reativando.maxxicredito.com.br**.

---

## 1) Criar conta GitHub e repositório
1. Crie/acesse sua conta em https://github.com
2. Clique em **New repository** → nome sugerido: `reativando-site`
3. **Não** marque para criar README/License por enquanto (vamos enviar os arquivos locais)
4. Crie o repositório (public ou private, tanto faz)

## 2) Clonar e subir os arquivos
> Requer Git instalado. No Windows, use o Git Bash ou PowerShell.

```bash
# 2.1) Clonar (troque USER pelo seu usuário)
git clone https://github.com/USER/reativando-site.git
cd reativando-site

# 2.2) Copiar todo o conteúdo do site para esta pasta (HTML, imagens, vercel.json etc.)

# 2.3) (Opcional) Definir o DOMÍNIO atual nos arquivos (ver seção 4)
# Exemplo: usar o domínio temporário da Vercel (reativando.vercel.app) antes do subdomínio final
python set-domain.py reativando.vercel.app

# 2.4) Commit & push
git add .
git commit -m "Reativando: primeira versão do site"
git push origin main
```

> **Observação:** Se o repositório criou a branch `master` em vez de `main`, ajuste o comando de push.

## 3) Conectar na Vercel (grátis)
1. Crie/acesse sua conta em https://vercel.com (login com GitHub facilita)
2. Clique em **Add New… → Project → Import Git Repository**
3. Selecione `reativando-site`
4. **Framework Preset:** “Other” (ou “Static Site”), sem build command, output = raiz do projeto
5. Deploy. Você receberá um domínio `*.vercel.app` (ex.: `reativando.vercel.app`)

## 4) Ajustar o DOMÍNIO nos arquivos (sitemap, robots e JSON-LD)
Este pacote inclui o script **`set-domain.py`** para substituir `{{DOMINIO}}` de forma segura.

```bash
# Ex.: definir o domínio provisório da Vercel
python set-domain.py reativando.vercel.app

# Ex.: depois, trocar para o subdomínio final
python set-domain.py reativando.maxxicredito.com.br
```

Arquivos afetados: `sitemap.xml`, `robots.txt` e blocos JSON-LD nos HTMLs.

## 5) Ativar o subdomínio depois
No projeto da Vercel: **Settings → Domains → Add** `reativando.maxxicredito.com.br`  
A Vercel vai mostrar um **CNAME alvo**. No seu provedor DNS, crie:
- **Host**: `reativando`
- **Tipo**: CNAME
- **Valor**: (exatamente o alvo exibido pela Vercel)
Depois da propagação, a Vercel vai emitir SSL automaticamente.

## 6) Testes rápidos pós-deploy
- `https://SEUDOMINIO/robots.txt` deve mostrar seu domínio
- `https://SEUDOMINIO/sitemap.xml` idem
- Teste os rich results (HowTo/FAQ/Breadcrumbs) no **Rich Results Test**
- Use Facebook Debugger e Twitter Card Validator para atualizar o cache de OG

## 7) Observações
- `vercel.json` inclui redirects úteis (ex.: `/descrição.html` → `/descricao.html`)
- Todos os vídeos estão com **youtube-nocookie.com**
- Páginas com **FAQ, HowTo, BreadcrumbList e VideoObject** para SEO

---

**Suporte**: Se precisar, me diga o nome do repositório criado e eu preparo os comandos exatos de push, ou gero uma versão já com o domínio final aplicado.