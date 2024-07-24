pipeline {
    agent any

    stages {
        stage('run backend server') {
            steps {
                dir ('C:\\users\\prath\\PycharmProjects\\June5\\ProjectOne'){

                bat 'start/min rest_app.py'
                bat 'start/min web_app.py'
                }

            }
        }
    }
}