pipeline {
    agent any // Define que o pipeline pode ser executado em qualquer agente disponível

    parameters {
        // Parâmetro de texto com nome "Pergunte:", description: 'perguntas.txt'
        string(name: 'Pergunte:', description: 'perguntas.txt')
        // Parâmetro de texto com nome "emailUsuario", description: 'E-mail do usuário', defaultValue: 'usuario@exemplo.com'
        string(name: 'emailUsuario', description: 'E-mail do usuário', defaultValue: 'usuario@exemplo.com')
        // Parâmetro de texto com nome "assuntoEmail", defaultValue: 'Resposta do Chatbot'
        string(name: 'assuntoEmail', defaultValue: 'Resposta do Chatbot')
        // Parâmetro de texto com nome "corpoEmail", defaultValue: 'Olá, \n\nSua pergunta foi: ${params.Pergunte}\n\nA resposta do chatbot é: [INCLUIR RESPOSTA DO CHATBOT]\n\nAtenciosamente,\nEquipe Chatbot'
        string(name: 'corpoEmail', defaultValue: 'Olá, \n\nSua pergunta foi: ${params.Pergunte}\n\nA resposta do chatbot é: [INCLUIR RESPOSTA DO CHATBOT]\n\nAtenciosamente,\nEquipe Chatbot')
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
                bat 'python chat_bot.py ${params.Pergunte}' // Executando o chatbot com a pergunta do usuário como entrada
                storeVars([ // Armazenando a resposta do chatbot em uma variável
                    'respostaChatbot': bat(script: 'return $LASTEXITCODE') // Capturando o código de saída do chatbot (que contém a resposta)
                ])
            }
        }

        stage('Enviar E-mail de Resposta') {
            steps {
                script {
                    // Substituindo a placeholder "[INCLUIR RESPOSTA DO CHATBOT]" no corpo do e-mail
                    def corpoEmailCompleto = params.corpoEmail.replace("[INCLUIR RESPOSTA DO CHATBOT]", respostaChatbot)

                    // Enviar e-mail de resposta
                    email(
                        to: params.emailUsuario,
                        subject: params.assuntoEmail,
                        body: corpoEmailCompleto
                    )
                }
            }
        }
    }
}

