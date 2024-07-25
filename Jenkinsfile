pipeline {
    agent any

    stages {
        stage('run backend server') {
            steps {
                dir ('C:\\users\\prath\\PycharmProjects\\June5\\ProjectOne'){

                bat 'start/min rest_app.py'
                bat 'start/min web_app.py'
                bat 'backend_testing.py'
5.              bat 'frontend _testing.py'
6.              bat 'combined_testing.py'
7.              bat 'clean_environment.py'
                }

            }
        }
    }
}