pipeline {
    agent any

    parameters {
        choice(
            name: 'TEST_TYPE',
            choices: ['api', 'ui', 'all'],
            description: 'Выбери, какие тесты запускать'
        )
    }

    environment {
        PYTHON = 'python3'
        VENV = 'venv'
        ALLURE_RESULTS = 'allure-results'
        ALLURE_REPORT = 'allure-report'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/oneearjoe/OTUS-FINAL-PROJECT.git'
            }
        }

        stage('Prepare Environment') {
            steps {
                sh '''
                    ${PYTHON} -m venv ${VENV}
                    . ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Clean Reports') {
            steps {
                sh '''
                    rm -rf ${ALLURE_RESULTS} ${ALLURE_REPORT}
                    mkdir -p ${ALLURE_RESULTS}
                '''
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    sh ". ${VENV}/bin/activate"

                    if (params.TEST_TYPE == 'api') {
                        sh "pytest tests/api --alluredir=${ALLURE_RESULTS}"
                    } else if (params.TEST_TYPE == 'ui') {
                        sh "pytest tests/ui --alluredir=${ALLURE_RESULTS} --browser=chrome --remote"
                    } else {
                        sh "pytest tests --alluredir=${ALLURE_RESULTS}"
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh "allure generate ${ALLURE_RESULTS} -o ${ALLURE_REPORT} --clean"
            }
        }

        stage('Publish Allure Report') {
            steps {
                allure([
                    includeProperties: false,
                    jdk: '',
                    results: [[path: "${ALLURE_RESULTS}"]]
                ])
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/example.log', allowEmptyArchive: true
        }
        failure {
            echo "❌ Тесты упали!"
        }
        success {
            echo "✅ Все тесты прошли успешно!"
        }
    }
}
