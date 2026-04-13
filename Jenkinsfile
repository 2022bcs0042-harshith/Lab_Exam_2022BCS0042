pipeline {
    agent any

    stages {

        stage('Setup') {
            steps {
                echo "Setting up virtual environment..."

                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Train') {
            steps {
                echo "Running training..."

                sh '''
                . venv/bin/activate
                python train.py
                '''
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