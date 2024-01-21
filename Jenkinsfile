pipeline {
    agent any
    
    stages {
        
        stage("code"){
            steps{
                git url: "https://github.com/billahmustasin/brainstations23.git", branch: "main"
                echo 'code cloned'
            }
        }
        stage("build and test"){
            steps{
                sh "docker build -t weather:latest ."
                echo 'code builded'
            }
        }
        stage("push"){
            steps{
                script {

                    def releaseVersion = sh(script: 'curl -s https://api.github.com/repos/billahmustasin/brainstations23/releases/latest | jq -r .tag_name', returnStdout: true).trim()
                    env.releaseversion = "$releaseVersion"
                    withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker tag weather:latest ${env.dockerHubUser}/weather:${releaseVersion}"
                    sh "docker push ${env.dockerHubUser}/weather:${releaseversion}"
                }
            }
        }
    }
    stage('environment and deploy') {
        environment {
        aws_access_key_id = credentials('aws_access_key')
        aws_secret_access_key = credentials('aws_secret_access_key')
        app_name = "api-application"
    }
    steps {
        script {
            echo 'hello'
            sh 'envsubst < kubernetes/deployment.yaml | kubectl apply -f -'
            sh 'envsubst < kubernetes/service.yaml | kubectl apply -f -'
        }
     }
  }
 }
}