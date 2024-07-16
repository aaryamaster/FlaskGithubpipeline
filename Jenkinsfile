pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "aariamaster/jenkins-pipeline" // Replace with your Docker image name
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
                    docker.build(DOCKER_IMAGE)
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE).inside {
                        sh 'pytest'
                    }
                }
            }
        }
        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', '6002f46a-c471-4c17-b02b-551f37c97e6f') {
                        docker.image(DOCKER_IMAGE).push()
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
