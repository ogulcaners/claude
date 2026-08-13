# Agency Agents — Kaynak ve Lisans Notu

Bu dizin, [`msitarzewski/agency-agents`](https://github.com/msitarzewski/agency-agents) deposundan alınan Claude Code alt-ajan (subagent) tanımlarının sürüm kontrollü bir kopyasıdır.

- **Kaynak commit**: `ebe9c99acb5c96f9468de368d8bead775387d1a7`
- **Alınma tarihi**: 2026-08-13
- **Lisans**: MIT (bkz. `LICENSE` bu dizinde — telif bildirimi: "Copyright (c) 2025 AgentLand Contributors")
- **İçerik**: 255 alt-ajan tanımı (`.md`, sadece prompt/kişilik tanımları — çalıştırılabilir kod içermiyor), 17 bölüme (division) ayrılmış: academic, design, engineering, finance, game-development, gis, healthcare, marketing, paid-media, product, project-management, sales, security, spatial-computing, specialized, support, testing.
- **Kurulum yöntemi**: Üst deponun `scripts/install.sh --tool claude-code` betiği, bu dizindeki dosyaları düz (flatten) biçimde `~/.claude/agents/` altına kopyalar. Aynı işlem bu oturumda manuel olarak (script çalıştırılmadan, sadece `cp` ile) yapıldı — betiğin kendisi bu depoya dahil edilmedi, çünkü sürüm kontrolü için sadece ajan tanımlarının kendisi gerekli.
- **Güvenlik notu**: Depo incelendi — `install.sh`/`convert.sh` betiklerinde curl|bash, sudo, uzak kod indirme gibi riskli örüntü yok; `rm -rf` kullanımları yalnızca betiğin kendi ürettiği çıktı dizinleriyle sınırlı. `SECURITY.md` ajan dosyalarının çalıştırılabilir kod veya kimlik bilgisi içermemesini şart koşuyor. Bu, `AUDIT-REPORT-2026-07-17.md`'deki denetim kriterleriyle (üçüncü taraf MCP sunucusu değil, salt metin/prompt tanımı; kod çalıştırma riski yok) tutarlıdır.

## Kullanım

`~/.claude/agents/` altına (flat, bölüm alt klasörü olmadan) kopyalanıp Claude Code'un yerleşik alt-ajan mekanizmasıyla (Agent tool) kullanılabilir hale getirildi. Bu depo klonlandığında yeniden kurmak için:

```bash
mkdir -p ~/.claude/agents
cp claude-config/agents/*/*.md ~/.claude/agents/
```

Güncellemek için üst depodan (`msitarzewski/agency-agents`) yeni bir `--depth 1` klon alıp bu dizini yeniden oluşturun ve yukarıdaki commit hash'ini güncelleyin.
