![Homer Simpson](assets/homer_simpson_doh.png)

# D'oh!

Fix command error instantly!

## Installation

```bash
alias doh='echo ''"''$(history | tail -n2 | head -n1 | sed "s/^ *[0-9]* *//")''"'
```

## Example

```
$ git push
fatal: The current branch test has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin test

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.
$ doh
Select a command:
 git push --set-upstream origin test
 # cancel
```