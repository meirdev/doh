from doh.command import Command
from doh.main import find_possible_corrects


def test_find_possible_corrects():
    cmd = Command(
        ["git", "push"],
        stdout=b"",
        stderr=b"""fatal: The current branch test has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin test

To have this happen automatically for branches without a tracking
upstream, see 'push.autoSetupRemote' in 'git help config'.""",
        exit_code=128,
    )

    for correct in find_possible_corrects(cmd):
        assert correct.args == ["git", "push", "--set-upstream", "origin", "test"]
