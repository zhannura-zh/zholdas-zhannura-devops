# DevOps laboratory for Zhannura Zholdas

Name: Zhannura  
Surname: Zholdas  
Group: IT2-2306  
Student ID: 37742  
Course: DevOps

This project demonstrates Linux file operations, permissions and processes; meaningful Git history and a development merge; a Python HTTP service; Docker and Compose; and delivery with Jenkins.

## Quick start in Ubuntu

```bash
git clone https://github.com/zhannura-zh/zholdas-zhannura-devops.git
cd zholdas-zhannura-devops
bash scripts/prepare_lab.sh
python3 -m unittest discover -s tests -v
docker compose up -d --build
python3 scripts/check_deployment.py
docker compose down
```

The service exposes `/`, `/student` and `/health` on port 8000. Unknown paths return 404. All four `STUDENT_*` environment variables override defaults. Empty values use the personalized defaults. IDs remain strings, including leading zeros. `APP_PORT` overrides the port in `config/app.conf`; `APP_CONFIG` selects another configuration file. Valid ports are 1 through 65535.

## Delivery

The exact job name is `Zholdas_Zhannura_DevOps`. Use Pipeline script from SCM, Git, the repository URL above, branch `*/main`, and script path `Jenkinsfile`. The stages are Checkout, Build, Test, Docker Build and Docker Run. Jenkins needs Python 3, Git, Docker access and the Pipeline/Git plugins. The image receives an OCI source revision label. The final stage checks health, every identity field and the deployed revision. A failure stops the following stages and prevents a successful build result.

The image is `zholdas-zhannura-devops` and the container is `zholdas-zhannura-container`. Manual, Compose and Jenkins demonstrations use the same container and port, so run them sequentially. Stop Compose before building in Jenkins. No webhook or automatic trigger is assumed: select Build Now after a push.

See `docs/COMMANDS.md` for explanations, `docs/VIDEO_SCRIPT.md` for the required personal recording and `docs/REQUIREMENTS.md` for the assignment map. The instructor submission includes real execution logs, screenshots, a PDF report, source archive and a separate Git history bundle. The student's continuous recording with their own voice remains a separate submission requirement.
