#!/usr/bin/env bash
set -euo pipefail

# Install system-wide aliases for interactive shells

PROFILE_D_FILE="/etc/profile.d/30-switchbox-aliases.sh"
cat > "${PROFILE_D_FILE}" <<'EOF'
# Switchbox aliases
alias ls='eza'
alias grep='ag'
EOF
chmod 0644 "${PROFILE_D_FILE}"

# zsh: prefer zshrc.d if present, else append once to /etc/zsh/zshrc
if [ -d /etc/zsh/zshrc.d ]; then
  ZSH_D_FILE="/etc/zsh/zshrc.d/30-switchbox-aliases.zsh"
  cat > "${ZSH_D_FILE}" <<'EOF'
# Switchbox aliases
alias ls='eza'
alias grep='ag'
EOF
  chmod 0644 "${ZSH_D_FILE}"
elif [ -f /etc/zsh/zshrc ]; then
  if ! grep -q "# _switchbox_aliases_begin" /etc/zsh/zshrc; then
    cat >> /etc/zsh/zshrc <<'EOF'
# _switchbox_aliases_begin
alias ls='eza'
alias grep='ag'
# _switchbox_aliases_end
EOF
  fi
fi
