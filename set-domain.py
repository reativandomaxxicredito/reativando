import sys, re, json, pathlib

def replace_domain_in_file(path: pathlib.Path, domain: str):
    text = path.read_text(encoding="utf-8")
    text2 = text.replace("{{DOMINIO}}", domain)
    if text2 != text:
        path.write_text(text2, encoding="utf-8")

def main():
    if len(sys.argv) != 2:
        print("Uso: python set-domain.py SEU.DOMINIO")
        sys.exit(1)
    domain = sys.argv[1].strip().lstrip("https://").lstrip("http://").rstrip("/")

    root = pathlib.Path(".")

    # 1) Substituir em sitemap.xml e robots.txt (se existirem)
    for fname in ["sitemap.xml", "robots.txt"]:
        p = root / fname
        if p.exists():
            replace_domain_in_file(p, domain)

    # 2) Substituir em HTMLs (inclusive JSON-LD embutido)
    for p in root.glob("*.html"):
        replace_domain_in_file(p, domain)

    print(f"Domínio aplicado: {domain}")

if __name__ == "__main__":
    main()