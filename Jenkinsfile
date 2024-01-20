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
        stage('Print Environment Variables') {
            steps {
                script {
                    sh 'env'
                }
            }
        }
        stage("push"){
            steps{
                script {

                    def releaseVersion = sh(script: 'curl -s https://api.github.com/repos/billahmustasin/brainstations23/releases/latest | jq -r .tag_name', returnStdout: true).trim()
                    echo "Release Version: ${releaseVersion}"
                    withCredentials([usernamePassword(credentialsId:"dockerHub",passwordVariable:"dockerHubPass",usernameVariable:"dockerHubUser")]){
                    sh "sed -i 's/RELEASE_VERSION/${releaseVersion}/' Dockerfile"
                    sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPass}"
                    sh "docker tag weather:latest ${env.dockerHubUser}/weather:${releaseVersion}"
                    sh "docker push ${env.dockerHubUser}/weather:${releaseVersion}"
                }
            }
        }
    }
}
}
