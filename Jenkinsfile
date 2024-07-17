pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "aaryamaster/jenkins-pipeline" // Replace with your Docker image name
        DOCKER_PATH = "/usr/local/bin/docker" // Replace with the actual path to the Docker executable
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: '5db5dac7-22bd-4d53-96a6-3944780c6c2a', url: 'https://github.com/aaryamaster/jenkinspipeline.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh "${DOCKER_PATH} build -t ${DOCKER_IMAGE} ."
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    sh "${DOCKER_PATH} run --rm ${DOCKER_IMAGE} pytest"
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: '6002f46a-c471-4c17-b02b-551f37c97e6f', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        sh "${DOCKER_PATH} login -u ${DOCKER_HUB_USERNAME} -p ${DOCKER_HUB_PASSWORD}"
                        sh "${DOCKER_PATH} push ${DOCKER_IMAGE}"
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
