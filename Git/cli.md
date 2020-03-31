# checkout
checkout == 대출 받는다. 다른 branch의 상태로 빌려온다.

```sh
# Checkout specific branch
$ git checkout <BRANCH>

# Checkout specific commit (detached from HEAD)
$ git checkout <COMMIT_ID>

# Restore specific file into unstaged state
# "--" stands to specify the next argument <FILE_PATH> is pointing file path
# For more information, check "ARGUMENT DISAMBIGUATION" in `man git-checkout`
$ git checkout -- <FILE_PATH>
```

# rebase
## Branch rebase
fork한 repo에서 내가 pull-request 하려 하는데, PR 이전에 repo에 commit이
더 추가되어 있다면, 추가된 내용에 대한 base commit을 추가해서 다시 commit을
올려야 하는 경우가 있다. 이 경우에 아래와 같은 순서로 command 처리하면 된다.

```sh
# Get upstream (community repo to send pull-request) commit bases
$ git fetch upstream master

# Rebase and merge upstream master comit bases
$ git rebase upstream/master

# Change rebased master branch into origin (remote repo for pull request)
$ git push origin master
```

## Interactive rebase
이전의 여러 commit을 수정하고 싶다면, rebase로 이전 commit들을 수정할 수 있다.

interactive rebase는 관련된 가장 최신 commit에서 edit 등을 걸어야 한다.

내 기억으로는 git에서 commit tree 관리가 linked list 식으로 구현되는데
그런 이유로 미래의 commit을 현재의 commit에서 관리할 수 없다.

```sh
# Start interactive rebase (COMMIT_ID must be parent of the desired commit)
$ git rebase -i <COMMIT_ID>

# Start interactive rebase (Use ^ to ref parent of the desired commit)
$ git rebase -i <COMMIT_ID>^
```

## Cancel rebase
Rebase 과정에서 오류가 났거나 원하지 않는 상태로 commit이 꼬인 경우, 아래
명령어를 사용하여 취소, 이전 상태로 되돌린다.

```sh
# Cancel rebase (when error occured, or trying to cancel curren progress)
$ git rebase --abort

# Restore branch to origin state
$ git reset --hard origin/master
```

# blame
blame을 이용하면 라인단위로 각 파일의 수정이 어느 commit에서 이루어졌는지 알 수
있다. 하지만 해당 commit 작성자가 해당 기능의 작성자라고 할 수 없다.

예를 들어, author A가 alpha에 대한 기능을 추가하여 0123456 이란 commit으로
올렸다. 그리고 author B가 alpha 기능에 관련된 코드를 리팩토링해서 7890abc로
commit해서 올렸다면 마치 alpha 기능의 책임자가 author B로 파악될 수 있다.
리팩토링 과정에서 버그가 있다면 이것은 author B가 실수한 것이지만, 원본
기능인 alpha 자체에 문제가 있었을 경우 author B는 해당 부분에 책임이 없으므로
관련 논의는 author A와 해야 한다.

만약 해당 코드 파일이 git mv와 같은 상태로 처리되었다면, blame시 파일 경로가
다르게 보인다. 파일 이전시, commit hash 옆에 파일 이름이 나타난다.

blame시 이전 commit의 file 상태를 보려면 아래와 같이 한다.
```sh
$ git blame <COMMIT_ID> <FILE>
```

# bisect
commit 단위의 이진 탐색을 통해 버그가 있는 commit을 찾는다.
