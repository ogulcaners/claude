#!/bin/bash
# claude-config/ yedeğini ~/.claude/ altına geri yükle
if [ -d claude/claude-config ]; then
  mkdir -p "$HOME/.claude/skills"
  cp claude/claude-config/CLAUDE.md "$HOME/.claude/CLAUDE.md"
  cp -r claude/claude-config/skills/. "$HOME/.claude/skills/"
fi
# ECC (everything-claude-code) tam kurulum, 2026-11-09 denetlenen surume sabit
ECC_DIR="$HOME/.cache/ecc"
ECC_REV=d2ef2680594f9a17526a6e1a2e18b3d242c5d17b
if [ ! -d "$ECC_DIR/.git" ]; then
  git init -q "$ECC_DIR"
  git -C "$ECC_DIR" remote add origin https://github.com/affaan-m/everything-claude-code.git
fi
if git -C "$ECC_DIR" fetch -q --depth 1 origin "$ECC_REV"; then
  git -C "$ECC_DIR" checkout -q FETCH_HEAD
  bash "$ECC_DIR/install.sh" --target claude --profile full --enable-hooks >/dev/null || echo "ECC kurulumu basarisiz"
fi
exit 0
