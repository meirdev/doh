![Homer Simpson](assets/homer_simpson_doh.png)

# D'oh!

Fix command error instantly!

## Installation

```bash
alias doh='echo ''"''$(history | tail -n2 | head -n1 | sed "s/^ *[0-9]* *//")''"'
```
