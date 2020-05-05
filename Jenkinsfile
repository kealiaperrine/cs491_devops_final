pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile sources/follow.py sources/monster.py sources/physics.py sources/player.py' 
                stash(name: 'compiled-results', includes: 'sources/*.py*') 
            }
        }
    }
}