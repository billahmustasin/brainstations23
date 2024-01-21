- Task: REST API with any language. Endpoint returning hostname, Datetime, version of the API or the application and return weather data for Dhaka using some free 3rd party weather API.

ANSWER: In the "app.py" file I have written a REST API with python language. I have used Flask framework. Here I have kept 3rd party weather API as secret which can be accessible with "os.environ.get('OPENWEATHER_API_KEY')".
======================
- Task: Create an endpoint to have some health checks.

ANSWER: I have added following endpoint for health check
#######
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'ok'})
======================
- Task: Containerize the application using docker. Ensure an optimized Docker file with security ensured.

ANSWER: I have containerized the application using "Dockerfile" which is in this repository's root directory.
======================
- Task: Make a public repository in GitHub.

ANSWER: Following is the public repository url: https://github.com/billahmustasin/brainstations23.git

======================
- Task: Use any CI/CD tool to design a pipeline.

ANSWER: Jenkins is used.

======================

- Task: The pipeline files should be in the repository.

ANSWER: I have kept pipeline file as "Jenkinsfile" which is in this repository's root directory.

======================
- Task: The Pipeline should run when a new release is created.

ANSWER: I have created a webhook with this repository to integrate with Jenkins and set the settings as "Which events would you like to trigger this webhook? > Let me select individual events > Releases (checked)"

======================

- Task: The release version should be used to create the docker image using the 
Docker file and push it to a public Docker Hub registry. This release version is the same one as the version when it returns the hello API

ANSWER: I am querying the GitHub API directly in Jenkins pipeline to get the release information.

======================

- Task: Write Terraform code to create a Kubernetes cluster in any cloud. We prefer to have a modular structure of Terraform Code and a remote Backend for Terraform state. Create a separate directory in the previously created public GitHub 
repository and put this code there.

ANSWER: I have kept all required code in "terraform-module-eks" directory. For Terraform state remote Backend I have used "S3" bucket which is in "terraform-module-eks/provider.tf" file.

======================

- Task: Create manifest files for Kubernetes in another directory in the public repo and prepare the CI/CD pipeline steps for deploying the app in the cluster. Ensure 3
rd party API credentials in secret or config map.

ANSWER: I have created manifest files for Kubernetes in "Kubernetes" directory which is in this repository's root directory.

# to deploy application with every release for dynamic image name I have set enviromental variable 

# to pass all enviromental variables to Kubernetes yaml files I have used command line tool "envsubst" 

# I had to install kubectl, aws-iam-authenticator & aws cli (to add aws credentials)

# inside "kubernetes/secret.yaml" file I have kept base 64 encoded 3rd party weather api key and used the reference in deployment file.

#####################