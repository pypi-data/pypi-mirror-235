current_merge_approvers = [
    "Cédric Fruteau De Laclos slipixel974@gmail.com",
    "Cédric Fruteau de Laclos fdlcdev@gmail.com",
    "Cédric Fruteau de Laclos cedric.fdl-ext@lupindental.com",
]

current_merge_approvers_mail = [
    approver.split(" ")[-1] for approver in current_merge_approvers
]

print(f"Current merge commit approvers: {current_merge_approvers_mail}")
child_commits_authors = ["cedric.fdl-ext@lupindental.com"]
print(f"Child commits authors: {child_commits_authors}")

# check if author of child commits is in current merge approvers
if any([author in current_merge_approvers_mail for author in child_commits_authors]):
    print(
        "Error: the author of the child commits is also an approver of the merge commit."
    )
