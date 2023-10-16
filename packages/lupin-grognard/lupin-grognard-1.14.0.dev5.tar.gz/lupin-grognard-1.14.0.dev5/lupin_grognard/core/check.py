import sys
from typing import List

from lupin_grognard.core.commit.commit import Commit
from lupin_grognard.core.commit.commit_error import ErrorCount
from lupin_grognard.core.commit.commit_validator import (
    CommitValidator,
    CommitCheckModes,
)
from lupin_grognard.core.tools.log_utils import die


def check_max_allowed_major_commits(
    commits: List[Commit], major_commit_limit: int
) -> bool:
    """Check if the number of major commits in `commits` exceeds `major_commit_limit`.

    Args:
        commits (List[Commit]): The list of commit object.
        major_commit_limit (int): The maximum number of major commits allowed.

    Returns:
        bool: True if the number of major commits is within the limit, else False.
    """
    if major_commit_limit == 0:  # --all option
        return True

    major_commit_count = 0
    for commit in commits:
        if commit.is_major_commit():
            major_commit_count += 1

    if major_commit_count > major_commit_limit:
        print(
            f"Error: found {major_commit_count} major commits to check in the "
            f"current branch while the maximum allowed number is {major_commit_limit}"
        )
        sys.exit(1)
    return True


def check_author_commits_is_not_approvers_current_merge(
    commits: List[Commit],
) -> None:
    """Check that the author of the child commits is not an approver of the merge commit

    Args:
        commits (List[Commit]): The list of commits to check.

    Returns:
        None
    """
    child_commits: List[Commit] = []
    merge_parent_found = False
    print(
        "Checking that the author of the child commits is not an approver of the merge commit"
    )
    if commits[0].title.startswith("Merge branch"):
        print(f"Found current merge commit: {commits[0].title}")
        for commit in commits[1:]:
            if commit.title.startswith("Merge branch"):
                merge_parent_found = True
            else:
                child_commits.append(commit)
            if merge_parent_found:
                current_merge_approvers = commits[0].approvers
                current_merge_approvers.append(
                    "Cédric Fruteau de Laclos cedric.fdl-ext@lupindental.com"
                )
                current_merge_approvers_mail = [
                    approver.split(" ")[-1] for approver in current_merge_approvers
                ]
                print(f"Current merge approvers: {current_merge_approvers_mail}")

                child_commits_authors = [
                    commit.author_mail
                    for commit in child_commits
                    if commit.author_mail not in child_commits_authors
                ]

                print(f"Child commits author: {child_commits_authors}")
                if any(
                    [
                        author in current_merge_approvers_mail
                        for author in child_commits_authors
                    ]
                ):
                    die(
                        msg=(
                            "The author of the child commits is also an approver of the merge commit."
                        )
                    )


def check_commit(
    commits: List[Commit],
    check_mode: CommitCheckModes,
    permissive_mode: bool,
    no_approvers: bool,
) -> None:
    """
    check_commit performs validation checks on each commit.
    If merge_option is set to 0, the function checks that merge commits
    have approvers.
    If merge_option is 1, the function only validates the title for a merge,
    the title and the body of the commit if it is a simple commit.
    The function also calls the error_report method of the ErrorCount
    class to output any errors found during validation.
    If any errors are found, it will call sys.exit(1)
    Args:
        commits (List): List of commits to check
        merge_option (int): 0 or 1
        permissive_mode (bool): If True, the function will not call sys.exit(1)
    """
    error_counter = ErrorCount()
    commits = [
        CommitValidator(
            commit=c,
            error_counter=error_counter,
            check_mode=check_mode,
            no_approvers=no_approvers,
        )
        for c in commits
    ]

    for commit in commits:
        commit.perform_checks()

    error_counter.error_report(
        permissive_mode=permissive_mode,
    )
