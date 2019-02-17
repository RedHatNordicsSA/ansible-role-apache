node() {
    try {
        stage ("Get Latest Code") {
            checkout scm
        }
        stage ("Install Application Dependencies") {
            sh 'sudo pip install --upgrade ansible==${ANSIBLE_VERSION} molecule==${MOLECULE_VERSION} docker'
        }
        stage ("Executing Molecule lint") {
            sh 'molecule lint'
        }
        stage ("Executing Molecule create") {
            sh 'molecule create'
        }
        stage ("Executing Molecule converge") {
            sh 'molecule converge'
        }
        stage ("Executing Molecule idemotence") {
            sh 'molecule idempotence'
        }
        stage ("Executing Molecule verify") {
            sh 'molecule verify'
        }
        stage ("Executing Molecule destroy") {
            sh 'molecule destroy'
        }
    } catch(all) {
        currentBuild.result = "FAILURE"
        throw err
    }
}
