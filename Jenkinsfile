pipeline {
    agent any

    stages {
        stage('run backend server') {
            steps {
                dir ('C:\\users\\prath\\PycharmProjects\\June5'){

//                     withEnv(['C:\\users\\prath\\PycharmProjects\\June5']) {
//                         bat 'start/min ProjectOne\\rest_app.py'
//                         bat 'start/min ProjectOne\\web_app.py'
//                      bat 'backend_testing.py'
//                      bat 'frontend _testing.py'
//                         bat 'ProjectOne\\combined_testing.py'
    //                  bat 'clean_environment.py'
                        echo $path
                        bat 'ProjectOne\\test.py'
//                     }
                }

            }
        }
    }
}