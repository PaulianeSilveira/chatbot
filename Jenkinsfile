pipeline {
    agent any  // Define que o pipeline pode ser executado em qualquer agente disponível

environment {
    PATH = "C:\\Windows\\System32;C:\\Users\\pauli\\AppData\\Local\\Programs\\Python\\Python312;C:\\Users\\pauli\\AppData\\Local\\Programs\\Python\\Python312\\Scripts;${env.PATH}"
}

    stages {
        stage('Preparação do Ambiente') {
            steps {
                echo 'Ambiente pronto'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                sh 'python3 levenshtein_teste.py'
            }
        }

        stage('Verificação do Arquivo de Perguntas') {
            steps {
                script {
                    if (fileExists('perguntas.txt')) {
                        echo 'Arquivo perguntas.txt encontrado!'
                    } else {
                        error('Arquivo perguntas.txt não encontrado. Interrompendo o pipeline.')
                    }
                }
            }
        }

        stage('Execução do Chatbot') {
            steps {
                sh 'python chat_bot.py'
            }
        }
    }
}
