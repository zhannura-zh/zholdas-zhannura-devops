# Commands and explanations

## Linux files and search

```bash
cd ~/devops/zholdas_zhannura
pwd
ls -la
mkdir -p backup/demo
touch backup/demo/original.txt
cp Zholdas_Zhannura_info.txt backup/demo/student_copy.txt
mv backup/demo/original.txt backup/demo/renamed.txt
rm backup/demo/renamed.txt
cat Zholdas_Zhannura_info.txt
head -n 3 logs/application.log
tail -n 5 logs/application.log
find . -name application.log
grep ERROR logs/application.log
grep WARNING logs/application.log
grep -c ERROR logs/application.log
```

`pwd` prints the working directory; `ls` lists entries; `cd` changes directory; `mkdir` creates directories; `touch` creates an empty file or updates its timestamp. `cp` copies; `mv` moves or renames; `rm` removes the named demonstration file; `cat` displays a complete file; `head` and `tail` select its beginning or end. `find` locates filenames recursively. `grep` selects matching lines and `-c` counts them. The prepared ten-line log has six INFO, two WARNING and two ERROR lines.

## Permissions and processes

```bash
chmod 600 private.txt
chmod 644 public.txt
ls -l private.txt public.txt
chmod +x scripts/Zholdas_Zhannura_system.sh
./scripts/Zholdas_Zhannura_system.sh
ps
ps aux
top -b -n 1
sleep 300 &
demo_pid=$!
ps -p "$demo_pid" -o pid,user,%cpu,%mem,comm
kill "$demo_pid"
```

The owner, group and others each have a permission digit: r=4, w=2 and x=1. Mode 600 gives the owner read/write and grants no access to group/others. Mode 644 adds group/others read access. Mode 755 gives the owner read/write/execute and everyone else read/execute; directories require execute permission for traversal. The private demonstration file models restricted data. The public demonstration file is safe to read. Git retains the executable bit but not full modes, so the preparation script restores 600 and 644 after cloning.

A process is an executing program with an operating-system process ID (PID). `ps` provides a snapshot; `top` refreshes live CPU and memory statistics. Terminate only the PID started for this demonstration. The Bash script prints whoami, hostname, date, uname, df and free, then checks the student file relative to its own location. Both file-existence branches should be explained.

## Git and GitHub

```bash
git config user.name
git config user.email
git status
git log --oneline --graph --all
git check-ignore logs/application.log backup/demo/student_copy.txt .env
git ls-files
git branch development
git switch development
# Make a meaningful source change and run the tests.
git add app/main.py tests/test_app.py
git commit -m "Handle termination and show delivery footer"
git switch main
git merge --no-ff development -m "Merge tested delivery improvements"
git remote -v
git push -u origin main development
git fetch origin
git pull --ff-only origin main
```

The local repository contains the working history. GitHub hosts a remote copy that Jenkins can retrieve. `push` sends local commits; `pull` fetches and integrates remote changes. A branch isolates changes until a merge brings them into main. The actual development branch is already included: do not recreate it without a new demonstration branch name. At least five commits must contain real changes. `.gitignore` excludes logs, backup/, .env and Python caches. `.env.example` is a safe tracked example. Ignoring a file does not untrack an already committed file.

## Docker and Compose

```bash
docker build -t zholdas-zhannura-devops .
docker images
docker run -d --name zholdas-zhannura-container -p 127.0.0.1:8000:8000 \
  -e STUDENT_NAME=Zhannura -e STUDENT_SURNAME=Zholdas \
  -e STUDENT_GROUP=IT2-2306 -e STUDENT_ID=37742 zholdas-zhannura-devops
docker ps
docker ps -a
docker logs zholdas-zhannura-container
docker exec zholdas-zhannura-container python --version
docker stop zholdas-zhannura-container
docker start zholdas-zhannura-container
docker stop zholdas-zhannura-container
docker rm zholdas-zhannura-container
cp .env.example .env
docker compose config
docker compose up -d --build
docker compose ps
python3 scripts/check_deployment.py
docker compose logs
docker compose down
```

An image is a reusable filesystem and runtime definition; a container is one instance with its own lifecycle and writable layer. FROM selects the base image, WORKDIR sets the working directory, COPY transfers build-context files, RUN executes during image creation, EXPOSE documents the service port and CMD selects the runtime command. EXPOSE does not publish a host port; `-p` does. Environment variables configure an instance without rebuilding the image. Never bake passwords into image layers. Compose defines service configuration once and consistently creates its container and network. Run Compose and Jenkins sequentially to prevent name/port conflicts.

## Jenkins and revision checks

```bash
git rev-parse HEAD
python3 -m compileall -q app tests
python3 -m unittest discover -s tests -v
docker inspect --format '{{ index .Config.Labels "org.opencontainers.image.revision" }}' zholdas-zhannura-container
python3 scripts/check_deployment.py
```

Jenkins retrieves the committed Jenkinsfile from GitHub, compiles, tests, builds an image and starts its container. The console prints name, surname, group, ID and SHA. Build success must be checked in Jenkins, then compared with GitHub/source SHA and the running image label. A manual Docker or Compose rebuild can replace the Jenkins image/container, so rebuild in Jenkins afterward before claiming revision alignment.
