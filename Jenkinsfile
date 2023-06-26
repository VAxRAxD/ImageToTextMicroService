pipeline{
    ''''
    1. Create a node in Jenkins for Kubernetes Server
    2. Assign label 'KOPS' to newly created node
    3. Add Kubernetes Server's private IP address and private key
    '''
    agent {label 'KOPS'}
    environment {
        registryCredential = 'ecr:us-east-1:AWS Credentials'
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
                        dockerImage.push("V$BUILD_NUMBER")
                        dockerImage.push('latest')
                    }
                }
            }
        }
        stage('Kubernetes Deploy'){
            steps{
                sh 'helm upgrade --install --force imgtxt-api helm/imgtxtcharts --namespace production'
            }
        }
    }
}