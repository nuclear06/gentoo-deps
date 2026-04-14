# gentoo-deps
repo for auto generate tarbar for gentoo ebuilds

## Triggers

- `workflow_dispatch`: manual generation, unchanged
- `issue_comment`: add a comment with `/approve` on a `deps-request` issue to start CI

## Issue workflow

1. Create a `Deps Request` issue.
2. Confirm the generated parameters.
3. Comment `/approve` as `saniter`.
4. CI generates the tarball release and closes the issue on success.
