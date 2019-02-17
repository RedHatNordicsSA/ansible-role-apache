node() {
    try {
        stage ("Get Latest Code") {
            checkout scm
        }
        stage ("Install Application Dependencies") {
            sh 'source ~/molecule_ansible27/bin/activate'
        }
        stage ("Executing Molecule lint") {
            sh 'molecule lint -s kvm'
        }
        stage ("Executing Molecule create") {
            sh 'molecule create -s kvm'
        }
        stage ("Executing Molecule converge") {
            sh 'molecule converge -s kvm'
        }
        stage ("Executing Molecule idemotence") {
            sh 'molecule idempotence -s kvm'
        }
        stage ("Executing Molecule verify") {
            sh 'molecule verify -s kvm'
        }
        stage ("Executing Molecule destroy") {
            sh 'molecule destroy -s kvm'
        }
    } catch(all) {
        currentBuild.result = "FAILURE"
        throw err
    }
}
