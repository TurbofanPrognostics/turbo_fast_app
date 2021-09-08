# turbo_fast_app
FourthBrain's AI/MLE May 2021 Cohort - FastAPI backend for turbofan engine failure app

# Run FastAPI on Docker
1. Install Docker on your machine: [Get Docker](https://docs.docker.com/get-docker/])
2. Build a docker image specified in this repo. First go to root of repo `/turbofan_fast_app` and run command: `docker build . -t turbofan_be`. Replace `turbofan_be` with any tag you would like.
3. To run the FastAPI server, run this command: `docker run --name turbo_fast -p 80:80 turbofan_be`. Note `turbo_fast` is the name of the docker image and `turbofan_be` is the container's tag from step 2.
4. See more docker runtime options here:
	- [FastAPI-Docker Github Repo](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker) 
	- [Deploy FastAPI with Docker Official Docs](https://fastapi.tiangolo.com/deployment/docker/)


# Deployment to AWS Elastic Beanstalk utilizing AWS CLI and EB CLI
1. Make sure you have the AWS CLI installed. Follow the steps (see pip commands) as shown on this guide: [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-windows.html). Make sure you are utilizing Python virtual environments ([Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/) so these libraries are installed outside of your system's Python environment.
2. Configure your AWS CLI: [AWS CLI Configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html). You will need an AWS Access KeyID and AWS Secrets Key from your AWS account administrator.
3. Install Elastic Beanstalk CLI (EB CLI) utilizing pip commands as shown here: [EB CLI Installation](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-windows.html). Make sure you are installing EB CLI in a Python virtual environment (same environment as AWS CLI was installed on).
4. Next, let's set up Elastic Beanstalk for deployment of this project. First go to the root directory of the project and type `eb init`. Make sure the virtual environment you installed AWS CLI and EB CLI is activated or else the command will not work.
5. `Select a default region.` This should match the region your AWS account is on.
6. `Select an application to use.` If this is the first time your application is being set up, pick `Create a new application` or just select the number that corresponds to the application you are trying to deploy.
7. `Enter application name.` Just create a unique name for your application.
8. `It appears you are using Docker. Is this correct?` Press `Y`.
9. `Do you wish to continue with CodeCommit? (Y/n):` Press `n`.
10. `Select a keypair.` Select a keypair that you have created before, or press `[ Create new KeyPair ]`.
11. Next enter `eb create`. Be sure you are still in the root directory for this repository.
12. `Enter Environment Name`. Hit `default` if your environment name is present.
13. `Enter DNS CNAME prefix`. Hit `default` if the name suffices.
14. `Select a load balancer type`. Enter `2` for `application`.
15. `Would you like to enable Spot Fleet requirements for this environmnet. Hit `N`.
Elastic Beanstalk should now create the environment and automatically deploy your app for consumption.
Use the command `eb terminate` and then enter the environment name to tear down the application off AWS Beanstalk. 
