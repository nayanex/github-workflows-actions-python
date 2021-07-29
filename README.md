# github-workflows-actions-python

In your root directory:

`mkdir -p ./.github/workflows`

Create a new GitHub Actions in the `./.github/workflows/docker-build.yml` that will build and push the Docker image for a Python web application, with the following requirements:

* Image name: `python-helloworld`
* Tag: `latest`
* Platforms: `platforms: linux/amd64,linux/arm64`

GitHub marketplace has a rich suite of upstream actions that can be easily integrated within a repository. One of the upstream action is [Build and Push Docker images](https://github.com/marketplace/actions/build-and-push-docker-images), which can be used to implement the required CI task.

The above GitHub action uses DockerHub Tokens and encrypted GitHub secrets to login into DockerHub and to push new images. To set up these credentials refer to the following resources:

* Create [DockerHub Tokens](https://www.docker.com/blog/docker-hub-new-personal-access-tokens/)
* Create [GitHub encrypted secrets](https://docs.github.com/en/free-pro-team@latest/actions/reference/encrypted-secrets)

**Note**: you will need a **Dockerfile** to build the image.