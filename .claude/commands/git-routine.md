# git-routine

This skill automates the standard git workflow for this project.

## Process
1. **Stage Changes**: Run `git add .` to stage all changes.
2. **Commit**: Generate a concise, descriptive commit message based on the current diff.
3. **Push**: Run `git push` to push the changes to the remote repository.

## Instructions for Claude Code
When the user invokes `/git-routine`, you should:
1. Check the current status and diff to understand what has changed.
2. Run `git add .`.
3. Craft a commit message that follows the project's style (if any) or is a clear summary of the changes.
4. Execute `git commit -m "<message>"`.
5. Execute `git push`.
6. Report the outcome (commit hash and push status) to the user.

**Important**: Ensure you use the attribution lines required by the project for commits:
`Co-Authored-By: Claude Code <noreply@anthropic.com>`
