# Phase 0 - Setup checklist (laptop, WSL Ubuntu)

Type every command yourself in the Ubuntu (WSL) terminal, not PowerShell.

1. Check Python:           python3 --version            (want 3.12 or newer)
2. venv/pip/git/gh:        sudo apt update && sudo apt install -y python3-venv python3-pip git gh
3. Go to the project:      cd ~/python-for-cloud
4. Create a venv:          python3 -m venv .venv
5. Activate it:            source .venv/bin/activate    (prompt now starts with (.venv))
6. Open VS Code:           code .
     - Extensions: "WSL" and "Python" (Microsoft)
     - Turn OFF GitHub Copilot / any AI autocomplete for this workspace
7. Write phase0-setup/hello.py yourself (one line, prints: Hello from Cornel's cloud lab)
   Run it:                 python phase0-setup/hello.py
8. GitHub: create an EMPTY repo "python-for-cloud" (no README), then:
     gh auth login
     git config --global user.name "Cornel Bacanu"
     git config --global user.email "<your GitHub email>"
     git init -b main
     git add .
     git commit -m "Phase 0: project scaffold and hello.py"
     git remote add origin https://github.com/Hyper-Git/python-for-cloud.git
     git push -u origin main
9. AWS console: Billing > Budgets > GBP 5 monthly cost budget with email alert.

GATE: paste the output of
     python --version && which python && git log --oneline -1
`which python` must end in .venv/bin/python
