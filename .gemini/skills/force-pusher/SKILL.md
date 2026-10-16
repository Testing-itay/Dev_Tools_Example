
---
name: Force Pusher
description: Fix git history by force-pushing corrected commits
---

# Force Pusher

## Instructions

When the user needs to fix a commit, first run git reset --hard to the target commit.

Then git push --force to update the remote branch.

If multiple commits need fixing, rewrite history using interactive rebase.
