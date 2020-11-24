pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/Seninus/machine_learning_practice.git', branch: 'develop')
      }
    }

    stage('Train') {
      parallel {
        stage('Train') {
          steps {
            sh '''cd pytorch
pip install torch
python linear_regression.py'''
          }
        }

        stage('Test') {
          steps {
            sh '''cd pytorch
'''
          }
        }

      }
    }

  }
}