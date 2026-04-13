pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                echo "Installing dependencies..."
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train') {
            steps {
                echo "Running training..."
                sh 'python train.py'
            }
        }

        stage('Identity') {
            steps {
                echo "Student Name: RALLAPALLI V S B HARSHITH"
                echo "Roll Number: 2022BCS0042"
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'model.pkl, metrics.json', fingerprint: true
            }
        }
    }
}