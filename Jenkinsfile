pipeline {
    agent any

    stages {
        stage('run backend server') {
            steps {
                dir ('C:\\users\\prath\\PycharmProjects\\June5'){

//                     withEnv(['C:\\users\\prath\\PycharmProjects\\June5']) {

                       bat 'start/min rest_app.py'
//                         bat 'start/min web_app.py'
//                      bat 'backend_testing.py'
                        bat 'frontend_testing.py'
//                         bat 'combined_testing.py'
    //                  bat 'clean_environment.py'

//                     }
                }

            }
        }
    }
}