def jobnameparts = JOB_NAME.tokenize('/') as String[]
def jobconsolename = jobnameparts[0]
def branchname = jobnameparts[1]
node() {
    try {
        sh 'env'
        deleteDir()    
	dir(ANSIBLE_ROLE_NAME){
	    stage ("Get Latest Code") {
		checkout scm
	    }
	    stage ("Executing Molecule lint") {
		sh """
		source ~/molecule_ansible27/bin/activate
		molecule lint -s kvm
		"""
	    }
	    stage ("Executing Molecule create") {
		sh """
		source ~/molecule_ansible27/bin/activate
		molecule create -s kvm
		"""
	    }
	    stage ("Executing Molecule converge") {
		sh """
		source ~/molecule_ansible27/bin/activate
		molecule converge -s kvm
		"""
	    }
	    stage ("Executing Molecule idemotence") {
		sh """
		source ~/molecule_ansible27/bin/activate
		molecule idempotence -s kvm
		"""
	    }
	    stage ("Executing Molecule verify") {
		sh """
		source ~/molecule_ansible27/bin/activate
		molecule verify -s kvm
		"""
	    }
	    stage ("Executing Molecule destroy") {
		sh """
		source ~/molecule_ansible27/bin/activate
		molecule destroy -s kvm
		"""
	    }
	}
    } catch(all) {
        currentBuild.result = "FAILURE"
        throw err
    }
}
