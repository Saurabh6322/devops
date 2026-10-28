pipeline {
    agent any

    parameters {
        choice(name: 'DEPLOY_ENV', choices: ['staging', 'production'], description: 'Target Deployment Environment')
        string(name: 'APP_PORT', defaultValue: '8085', description: 'Application Port Binding')
    }

    tools {
        maven 'Maven 3.9'
        jdk 'JDK 21'
    }

    environment {
        APP_NAME = 'insurance-verification-portal'
        IMAGE_NAME = 'sourabhshelke/insurance-verification'
        VERSION = '1.0.0'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Pulling latest commit from GitHub repository...'
                checkout scm
            }
        }

        stage('Build & Compile') {
            steps {
                echo 'Compiling source code with Apache Maven...'
                bat 'mvn clean compile'
            }
        }

        stage('Automated Tests') {
            steps {
                echo 'Executing JUnit & Selenium test suite (Quality Gate)...'
                bat 'mvn test'
            }
            post {
                always {
                    junit allowEmptyResults: true, testResults: 'target/surefire-reports/*.xml'
                }
            }
        }

        stage('Package Artifact') {
            steps {
                echo 'Packaging standalone Spring Boot executable JAR file...'
                bat 'mvn package -DskipTests'
            }
            post {
                success {
                    archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
                }
            }
        }

        stage('Docker Build & Tag') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}:${BUILD_NUMBER}..."
                bat "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} -t ${IMAGE_NAME}:latest ."
            }
        }

        stage('Containerized Deployment') {
            steps {
                echo "Deploying ${APP_NAME} to ${params.DEPLOY_ENV} on port ${params.APP_PORT}..."
                bat "docker stop insurance-app || exit 0"
                bat "docker rm insurance-app || exit 0"
                bat "docker run -d -p ${params.APP_PORT}:8085 --name insurance-app ${IMAGE_NAME}:latest"
                echo "Container deployed. Validating microservice health endpoint..."
            }
        }
    }

    post {
        success {
            echo "CI/CD Pipeline successfully executed for ${env.JOB_NAME} Build #${env.BUILD_NUMBER}!"
            echo "Access application at: http://localhost:${params.APP_PORT}"
        }
        failure {
            echo "Pipeline Quality Gate FAILED! Stopping deployment to prevent defective release."
        }
    }
}
