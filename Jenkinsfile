pipeline {
    agent any


    stages {
        stage('Build') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'master', url: 'https://github.com/JohnFirsthawk/django-project.git'

                
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv myvenv
                    source myvenv/bin/activate
                    pip install -r requirements.txt
                    cd myproject
                    cp myproject/.env.example myproject/.env
                    sed -i 's#^DATABASE_URL.*#DATABASE_URL=postgresql://dbuser:pass123@pg-cluster-ip/test_db#g' myproject/.env
                    python3 manage.py test'''
            }
        }
        stage('Deploy') {
            steps {
                sshagent (credentials: ['ssh-deployment-1']) {

                sh '''
                    pwd
                    echo $WORKSPACE
                    ansible-playbook -i ~/workspace/ansible-project/hosts.yml -l deploymentservers ~/workspace/ansible-project/playbooks/check.yml
                     '''
            }
            }
        }
    }
}
