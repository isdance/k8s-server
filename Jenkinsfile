pipeline {
  agent none
  environment {
    CI = 'true'
    HOME = '.'
  }
  stages {
    stage('setup') {
      agent { docker { image 'python:3.7.2' } }
      steps {
        sh 'make setup'
        sh '. ~/.server-proj/bin/activate'
      }
    }
    stage('lint') {
      agent { docker { image 'python:3.7.2' } }
      steps {
        sh 'make install'
        sh 'make lint'
      }
    }
    stage('Build Docker Image') {
      agent any
			steps {
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD']]){
					sh '''
						docker build -t isdance/server .
					'''
				}
			}
		}

		stage('Push Image To Dockerhub') {
      agent any
			steps {
				withCredentials([[$class: 'UsernamePasswordMultiBinding', credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD']]){
					sh '''
						docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD
						docker push isdance/server
					'''
				}
			}
		}
  }
}