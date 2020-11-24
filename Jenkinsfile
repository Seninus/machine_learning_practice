pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/Seninus/machine_learning_practice.git', branch: 'develop')
      }
    }

    stage('Train') {
      steps {
        sh '''cd pytorch
python linear_regression.py'''
      }
    }

  }
}