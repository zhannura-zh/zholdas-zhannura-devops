# Assignment map and verification plan

All statuses refer to evidence in the final submission package. Source implementation alone is not execution proof.

| Task | Required action | Personalized resource | Verification | Evidence | Figure | Report section | Status |
|---|---|---|---|---|---|---|---|
|1|Linux project and files|zholdas_zhannura, Zholdas_Zhannura_info.txt|pwd, ls, file operations|01_linux_files_search_permissions.txt|Linux files|Linux files|Executed|
|2|Search and logs|logs/application.log|find, grep, grep -c, tail|01_linux_files_search_permissions.txt|Linux files|Linux search|Executed|
|3|Permissions|private.txt, public.txt|stat 600 and 644|01_linux_files_search_permissions.txt|Linux files|Permissions|Executed|
|4|Bash system script|Zholdas_Zhannura_system.sh|run, missing/present branches, other cwd|02_linux_script_processes.txt|System script|Bash|Executed|
|5|Processes|temporary sleep PID|ps, ps aux, top, kill|02_linux_script_processes.txt|System script|Processes|Executed|
|6|Git repository and identity|Zhannura Zholdas|git status/config|06_git_history_ignore.txt|Git history|Git|Recorded in final evidence|
|7|Five meaningful commits|main history|git log|06_git_history_ignore.txt|Git history|Git|Recorded in final evidence|
|8|Ignore local data|*.log, backup/, .env|check-ignore and ls-files|06_git_history_ignore.txt|Git history|GitHub|Recorded in final evidence|
|9|Development and merge|development, main|git log --graph|06_git_history_ignore.txt|Git history|Git|Recorded in final evidence|
|10|GitHub repository|zholdas-zhannura-devops|remote, push and API SHA|07_github_repository.json|GitHub|GitHub|Recorded in final evidence|
|11|Dockerfile instructions|zholdas-zhannura-devops|docker build|04_docker_lifecycle_environment.txt|Docker environment|Dockerfile|Executed|
|12|Image and container|zholdas-zhannura-container|images, ps, ps -a|04_docker_lifecycle_environment.txt|Docker environment|Docker|Executed|
|13|Runtime variables|all four STUDENT values|exact JSON and demo override|04_docker_lifecycle_environment.txt|Docker environment|Environment|Executed|
|14|Container lifecycle|student container|logs, exec, stop/start/rm|04_docker_lifecycle_environment.txt|Docker environment|Lifecycle|Executed|
|15|Compose|docker-compose.yml|config, up, ps, logs, down|05_compose.txt|Compose|Compose|Executed|
|16|Jenkins job|Zholdas_Zhannura_DevOps|SCM job XML|08_jenkins_job.xml|Jenkins SCM|Jenkins|Recorded in final evidence|
|17|Five stages|Jenkinsfile|stage REST JSON|jenkins_build_*_stages.json|Jenkins stages|Pipeline|Recorded in final evidence|
|18|GitHub checkout|origin main|console checkout revision|jenkins_build_*_console.txt|Jenkins console|Pipeline|Recorded in final evidence|
|19|Jenkins variables|Zhannura Zholdas IT2-2306 37742|console identity|jenkins_build_*_console.txt|Jenkins console|Pipeline|Recorded in final evidence|
|20|Successful Pipeline|student job and image|SUCCESS and image label|09_final_verification.json|Jenkins stages|Verification|Recorded in final evidence|
|21|Integrated source change|development merge|push, new build, live footer|10_integrated_change.txt|Application|Integrated workflow|Recorded in final evidence|
|Submission|PDF and accessible repository|personalized report|archive and checksum verification|SHA256SUMS.txt|All figures|Conclusion|See final report|
|Video|Continuous recording with own voice|Zhannura Zholdas|student recording review|not yet recorded|None|Conclusion|PENDING|

The rubric is Linux 25, Git/GitHub 25, Docker 25, Jenkins 20 and Video 5. The detailed task points differ from the rubric totals, so every task must be demonstrated.
