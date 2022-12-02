pipeline {
                options { timestamps() }
                agent none
                stages {
                    stage('Check scm') {
                        agent any
                        steps {
                            checkout scm
                        }
                    }//stage Build
                    stage('Build') {
                        steps {
                        echo "Building...${BUILD_NUMBER}"
                        echo "Build completed"
                    }//stage Build
                }
                stage('Test') {
                    agent { docker { image 'alpine'
                        args '-u=\"root\"'
                        }
                    }
                steps {
                    sh 'apk add --update python3 py-pip'
                    sh 'pip install xmlrunner'
                    sh 'python3 unitTestCherga.py'
                }
                post {
                    always {
                        junit 'test-reports/*.xml'
                    }
                success {
                    echo "Application testing successfully completed "
                }
                failure {
                    echo "Oooppss!!! Tests failed!"
                }
            } // post
        } // stage Test
                 stage('Push') {

			            steps {
                    sh 'docker build -t bormaxv/jenkins .'
                    sh 'docker run -d -p 5000:5000 bormaxv/jenkins'
                    sh 'docker ps -a'
                    sh 'docker login -u ${{ secrets.login }} -p ${{ secrets.pass }}'
                    sh 'docker push bormaxv/deployment:latest'
			            }
		            }
    } // stages
}
