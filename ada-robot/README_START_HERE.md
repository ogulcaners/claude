# ADA Robot — Claude Architecture Pack

Bu paket, Yapada Kırtasiye'deki Mini Ada 3 mağaza robotunu tek parça ve şişmiş bir prompt yerine,
modüler, test edilebilir ve sürümlenebilir bir yapıya geçirmek için hazırlanmıştır.

## En önemli karar

Claude'a yüklemek için ana GitHub temeli:

**arpitg1304/robotics-agent-skills**

Bu repo Claude'un anlayabildiği `SKILL.md` biçiminde ROS1/ROS2, perception, test, security,
bringup, Docker ve web entegrasyonu bilgileri sağlar. Ancak mevcut sürümünde Nav2/navigation
skill'i henüz yol haritasındadır. Bu paketteki `ada-navigation` skill'i bu boşluğu Ada'nın
mağaza senaryosu için doldurur.

## Claude'a nasıl verilecek?

### Claude Projects / Claude.ai
1. Bu ZIP'i aç.
2. Tüm klasörü Claude Project'e yükle.
3. İlk mesaj olarak `MASTER_PROMPT_FOR_CLAUDE.md` dosyasının içeriğini gönder.
4. Varsa mevcut Akınrobotics promptlarını, logları, harita koordinatlarını, API/tool tanımlarını
   ve Gemini araştırmasını aynı projeye ekle.
5. Claude'dan önce audit, sonra mimari, sonra değişiklik planı istemeden doğrudan kod yazdırma.

### Claude Code
1. Proje köküne bu paketin içeriğini kopyala.
2. `.claude/skills/` altındaki özel Ada skill'leri otomatik keşfedilebilir.
3. Harici robotics skill paketini ayrıca kur:
   ```bash
   git clone https://github.com/arpitg1304/robotics-agent-skills.git
   cd robotics-agent-skills
   ./install.sh \
     --target /PATH/TO/ADA_PROJECT/.claude/skills \
     --skills ros2 robotics-software-principles robotics-design-patterns \
              robot-perception robotics-testing docker-ros2-development \
              ros2-web-integration robot-bringup robotics-security
   ```
4. Claude Code'u Ada projesinin kökünde çalıştır.
5. `MASTER_PROMPT_FOR_CLAUDE.md` içeriğini ilk görev olarak ver.

## Dosya grupları

- `CLAUDE.md`: Claude'un proje boyunca uyması gereken çalışma anayasası.
- `.claude/skills/`: Ada'ya özel modüler Claude skill'leri.
- `architecture/`: hedef mimari ve katmanlar.
- `prompts/`: runtime prompt ve geliştirme promptları.
- `configs/`: mağaza haritası, intent router, güvenlik, model routing.
- `schemas/`: tool call ve robot state JSON şemaları.
- `behavior_trees/`: deterministik yürütme ve recovery örnekleri.
- `evals/`: promptfoo benzeri test/eval örnekleri.
- `docs/`: GitHub araştırması, kabul kriterleri, rollout ve failure mode listesi.

## Temel mimari ilkesi

LLM fiziksel motor komutu üretmemelidir.

Doğru zincir:

`SENSE -> UNDERSTAND -> ROUTE -> PLAN -> VALIDATE -> EXECUTE -> VERIFY -> RECOVER -> REPORT`

Claude/LLM yalnızca sınırlı ve şemalı yüksek seviyeli niyet üretir. Navigasyon, motor kontrolü,
çarpışma önleme, emergency stop ve donanım limitleri deterministik katmanlarda kalır.
