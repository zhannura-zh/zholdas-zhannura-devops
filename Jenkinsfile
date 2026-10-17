pipeline {
    agent any
    options { skipDefaultCheckout(true); disableConcurrentBuilds(); timestamps() }
    environment {
        STUDENT_NAME = 'Zhannura'
        STUDENT_SURNAME = 'Zholdas'
        STUDENT_GROUP = 'IT2-2306'
        STUDENT_ID = '37742'
        IMAGE_NAME = 'zholdas-zhannura-devops'
        CONTAINER_NAME = 'zholdas-zhannura-container'
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                sh '''echo "Student: $STUDENT_NAME $STUDENT_SURNAME"
echo "Group: $STUDENT_GROUP"
echo "Student ID: $STUDENT_ID"
git rev-parse HEAD'''
            }
        }
        stage('Build') { steps { sh 'python3 -m compileall -q app tests scripts/check_deployment.py' } }
        stage('Test') { steps { sh 'python3 -m unittest discover -s tests -v' } }
        stage('Docker Build') {
            steps { sh 'docker build --label org.opencontainers.image.revision=$(git rev-parse HEAD) -t "$IMAGE_NAME" .' }
        }
        stage('Docker Run') {
            steps {
                sh '''if docker container inspect "$CONTAINER_NAME" >/dev/null 2>&1; then
  docker rm -f "$CONTAINER_NAME"
fi
docker run -d --name "$CONTAINER_NAME" -p 127.0.0.1:8000:8000 \
  -e STUDENT_NAME -e STUDENT_SURNAME -e STUDENT_GROUP -e STUDENT_ID "$IMAGE_NAME"
python3 scripts/check_deployment.py
test "$(git rev-parse HEAD)" = "$(docker inspect --format '{{ index .Config.Labels "org.opencontainers.image.revision" }}' "$CONTAINER_NAME")"
docker ps --filter name="$CONTAINER_NAME"'''
            }
        }
    }
}
