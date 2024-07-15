pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "your-dockerhub-username/demo-flask-app"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/SOWMYAganuga/PythonFlaskApp.git'
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
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Add your deployment steps here, e.g., deploying to a server or Kubernetes cluster
                    sh 'echo "Deploying to server..."'
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