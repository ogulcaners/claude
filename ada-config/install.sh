#!/usr/bin/env bash
# Ada skill kurulum scripti — arpitg1304/robotics-agent-skills'teki install.sh deseninden uyarlanmıştır.
# Kullanım:
#   ./install.sh --target /path/to/.claude/skills --skills order-tracking-inquiry returns-refunds
#   ./install.sh --target /path/to/.claude/skills --skills all
#   ./install.sh --list

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="${SCRIPT_DIR}/skills"

DEFAULT_SKILLS=(ada-conversation-principles order-tracking-inquiry human-handoff-escalation customer-data-privacy-kvkk)

usage() {
  cat <<EOF
Kullanım: $0 --target <dizin> [--skills <isim1> <isim2> ... | all]

Seçenekler:
  --target <dizin>   Skillerin kopyalanacağı .claude/skills/ dizini (zorunlu)
  --skills <isim...> Kurulacak skill adları, ya da "all". Belirtilmezse varsayılan set kurulur:
                      ${DEFAULT_SKILLS[*]}
  --list             Mevcut skilleri listele ve çık
  --help             Bu yardım metnini göster

Örnek (tam kapsam):
  $0 --target ~/.claude/skills --skills all
EOF
}

list_skills() {
  echo "Mevcut Ada skilleri:"
  for d in "${SKILLS_DIR}"/*/; do
    name="$(basename "${d}")"
    echo "  - ${name}"
  done
}

TARGET=""
SKILLS=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target)
      TARGET="$2"; shift 2 ;;
    --skills)
      shift
      while [[ $# -gt 0 && "$1" != --* ]]; do
        SKILLS+=("$1"); shift
      done ;;
    --list)
      list_skills; exit 0 ;;
    --help)
      usage; exit 0 ;;
    *)
      echo "Bilinmeyen argüman: $1" >&2
      usage; exit 2 ;;
  esac
done

if [[ -z "${TARGET}" ]]; then
  echo "Hata: --target zorunludur." >&2
  usage
  exit 2
fi

if [[ ${#SKILLS[@]} -eq 0 ]]; then
  SKILLS=("${DEFAULT_SKILLS[@]}")
fi

if [[ "${SKILLS[0]:-}" == "all" ]]; then
  SKILLS=()
  for d in "${SKILLS_DIR}"/*/; do
    SKILLS+=("$(basename "${d}")")
  done
fi

mkdir -p "${TARGET}"

for skill in "${SKILLS[@]}"; do
  src="${SKILLS_DIR}/${skill}"
  if [[ ! -d "${src}" ]]; then
    echo "Hata: bilinmeyen skill '${skill}'." >&2
    list_skills
    exit 1
  fi
  cp -r "${src}" "${TARGET}/"
  echo "Kuruldu: ${skill}"
done

echo "Tamamlandı. ${#SKILLS[@]} skill '${TARGET}' dizinine kopyalandı."
