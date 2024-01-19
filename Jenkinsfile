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
                sh "docker build -t weather ."
                echo 'code builded'
            }
        }
        stage("scan image"){
            steps{
                echo 'image scanned'
            }
        }
    }
}
