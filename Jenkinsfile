pipeline {
  
    agent any

    stages {
      
        stage('Build') {
          
            steps {
              sh pip install -r ./requirements.txt
              sh python manage.py runserver
            }
        }
      
        stage('Test') {
          
            steps {
              sh python manage.py test
            }
        }
    }
}
