pipeline {
    agent any  // Define que o pipeline pode ser executado em qualquer agente disponível
    parameters {
        // Parâmetro de texto com nome "nomeDoArquivo" e valor padrão "perguntas.txt"
        string(name: 'Pergunte:', description: 'perguntas.txt')
    }


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
                bat 'python levenshtein_teste.py'
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
                bat 'python chat_bot.py'
            }
        }
    }
}
