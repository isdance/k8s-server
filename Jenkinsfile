pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'make setup'
        sh 'source ~/.server-proj/bin/activate'
        sh 'make install'
      }
    }
    stage('lint') {
      steps {
        sh 'make lint'
      }
    }
  }
}