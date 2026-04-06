@Library('Shared_demo')_ 
pipeline {
    agent { label 'agent-56-11' }

    stages {
        stage('Code') {
            steps{
                echo "This is cloning the code"
                git url: "https://github.com/Devendra-Singh6464/Django-api.git",  branch:'main'
                echo "This is cloning successfully"
            }
        }
        stage('Build'){
            steps{
                echo "This is Build the code"
                // Run in detached mode (-d) so it doesn't block the pipeline
                // Removed the invalid '.' at the end
                sh 'docker compose up -d --build'
            }
        }
        stage('Test'){
            steps{
                echo "This is Testing the code"
                // E.g., sh 'docker compose exec -T web python manage.py test'
            }
        }
        stage('Cleanup'){
            steps{
                echo "Tearing down the containers"
                sh 'docker compose down'
            }
        }
    }
}
