@Library('ProjectOne')
import webdriver
import Service
import By
import requests
import pymysql
import time

pipeline {
    agent any

    stages {
        stage('run backend server') {
            steps {
                dir ('C:\\users\\prath\\PycharmProjects\\June5\\ProjectOne'){

//                     withEnv(['C:\\users\\prath\\PycharmProjects\\June5']) {
//                         bat 'start/min ProjectOne\\rest_app.py'
//                         bat 'start/min ProjectOne\\web_app.py'
//                      bat 'backend_testing.py'
//                      bat 'frontend _testing.py'
                         bat 'combined_testing.py'
    //                  bat 'clean_environment.py'
                        bat 'ProjectOne\\test.py'
//                     }
                }

            }
        }
    }
}