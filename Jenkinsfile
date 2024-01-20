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
                    withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker tag weather:latest ${env.dockerHubUser}/weather:${BUILD_ID}"
                    sh "docker push ${env.dockerHubUser}/weather:${BUILD_ID}"
                }
            }
        }
    }
}
}
