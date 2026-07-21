# Güvenlik Denetimi ve Kurulum Kararları — 2026-07-21

2 harici GitHub deposu, salt-okunur denetim (git clone --depth 1 + Read/Grep, hiçbir install/setup scripti çalıştırılmadı) ile incelendi. Bu, 2026-07-17 tarihli 18 depoluk denetimin kapsamı dışında kalan, kullanıcının bu oturumda ayrıca talep ettiği iki yeni bileşen içindir. Bkz. `AUDIT-REPORT-2026-07-17.md` için karar mantığı ve önceki bulgular — bu iki depo o listede yer almıyordu.

## Depo Bazında Özet

| Depo | Tür | Karar | Gerekçe |
|---|---|---|---|
| AThevon/genjutsu | Bireysel, MIT | **Kuruldu** | Creative-coding/motion-design skill paketi (`cast`, `paint` + 13 alt-skill `_jutsu/` altında). Sadece Markdown talimat dosyaları + 3 Python scripti (`ui-ux-pro-max/scripts/`) incelendi: scriptler yalnızca standart kütüphane kullanıyor (`csv`, `json`, `os`, `math`, `collections`, `pathlib`, `datetime`, `argparse`, `sys`, `io`) — ağ çağrısı, `subprocess`/`eval`/`exec`, veya kimlik bilgisi toplama yok. `password`/`token`/`secret` eşleşmeleri incelendiğinde hepsi zararsız bağlamda (UI pattern kategorileri, design token, metin tokenization) çıktı. Akademik araştırma iş akışıyla çakışmıyor — farklı alan (tasarım/motion). **Bilinen kısıt**: `cast`/`paint` alt-skill'leri, `~/.claude/plugins/**/genjutsu/skills` altında bir plugin kurulumu veya claude.ai'da `/mnt/skills/user/` altında yükleme bekleyen bir `SKILL_BASE` yol çözümlemesi kullanıyor. Doğrudan `~/.claude/skills/` altına kopyalama (bu kurulum yöntemi) bu iki koşulu karşılamıyor; bu nedenle `cast`/`paint` orkestratörlerinin alt-skill yükleme adımı (`$SKILL_BASE/...`) çalışma zamanında boş yol üretebilir. `_jutsu/` altındaki alt-skill'ler yine de doğrudan Skill aracıyla ayrı ayrı çağrılabilir durumda. Kullanıcı isterse resmi plugin marketplace yolu (`/plugin marketplace add AThevon/genjutsu`) ile yeniden kurulum önerilir. |
| zanwei/design-dna | Bireysel, MIT | **Kuruldu** | Tek dosyalı skill (`SKILL.md` + 2 referans Markdown). Kod içermiyor (script/binary yok) — 3 fazlı bir analiz/üretim iş akışı tanımlıyor (tasarım tokenlarını çıkar, JSON'a yapılandır, içeriğe uygula). Ağ/kimlik bilgisi/exec deseni taraması temiz çıktı. Akademik araştırma alanıyla ilgisi yok ama zararsız ve kapsamı net. |

## Kurulan Bileşenler (bu denetim)

- **genjutsu** (`~/.claude/skills/cast/`, `~/.claude/skills/paint/`, `~/.claude/skills/_jutsu/*`)
- **design-dna** (`~/.claude/skills/design-dna/`, orijinal git geçmişiyle — depo yedeğinde `claude-config/skills/design-dna/` içine `.git` hariç kopyalandı)

## Not

Bu iki skill, `claude-config/CLAUDE.md`'de tanımlanan 7 akademik skill'in kapsamı dışındadır (tasarım/creative-coding amaçlı, kullanıcının ayrı bir talebi üzerine eklendi). Akademik dürüstlük ve kaynak doğrulama kuralları bu skill'ler için geçerli değildir çünkü onlarla ilgisi yoktur.
