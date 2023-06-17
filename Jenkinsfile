pipeline{
    agent any
    environment {
        registryCredential = 'ecr:us-east-1:awscred'
        appRegistry = "031677989988.dkr.ecr.us-east-1.amazonaws.com/img-txt-microservice"
        microserviceRegistry = "https://031677989988.dkr.ecr.us-east-1.amazonaws.com"
    }
    stages {
        stage('Fetch code'){
            steps {
                git branch: 'master', url: 'https://github.com/VAxRAxD/ImageToTextMicroService.git'
            }
        }
        stage('Build App Image') {
            steps {
                script {
                    dockerImage = docker.build( appRegistry + ":$BUILD_NUMBER", ".")
                }
            }
        }
        stage('Upload App Image') {
            steps{
                script {
                    docker.withRegistry( microserviceRegistry, registryCredential) {
                        dockerImage.push("$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
    }
}