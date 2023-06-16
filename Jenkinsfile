pipeline{
    agent any
    stages{
        stage('Fetch Code'){
            steps{
                git branch:'master',url:'https://github.com/VAxRAxD/ImageToTextMicroService.git'
            }
        }
        stage('Build Image'){
            steps{
                sh 'docker build -t api-microservice .'
                sh 'docker stop microservice-container &> /dev/null && docker rm microservice-container &> /dev/null'
                sh 'docker run -d --name microservice-container -p 8000:8000 api-microservice'
            }
        }
    }
}