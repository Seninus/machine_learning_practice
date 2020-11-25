pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps {
        git(url: 'https://github.com/Seninus/machine_learning_practice.git', branch: 'develop')
      }
    }

    stage('Train Model') {
      parallel {
        stage('Test') {
          steps {
            sh '''cd pytorch

sudo -i
sudo apt-get install python3-pip python-dev
python --version

pip install torch
python linear_regression.py'''
          }
        }

        stage('Train') {
          steps {
            sh '''cd pytorch
'''
          }
        }

      }
    }

    stage('Eval Metric') {
      steps {
        echo 'metrics is good'
      }
    }

  }
}