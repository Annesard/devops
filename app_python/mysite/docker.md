# Docker best practices

There are a lot of issues that could happend if you use docker especially security one. Below are listed best docker practices that help to prevent them:

## 1. Avoid unnecessary privileges
 * Rootless containers: make sure not to leave the container with root rights.
 * Don’t bind to a specific UID: openshift, by default, will use random UIDs when running containers
 * Make executables owned by root and not writable
 ## 2. Reduce attack surface
 * Multistage builds
 * Distroless, from scratch
 * Use trusted base images
 * Update your images frequently
 * Exposed ports
 ## 3. Prevent confidential data leaks
 * Credentials and confidentiality : never put any secret or credentials in the Dockerfile instructions
 * ADD, COPY: Use COPY unless you really need the ADD functionality, like to add files from an URL or from a tar file.
 * Build context and dockerignore
 ## Others
 * Layer sanity
 * Metadata labels
 * Linting
 * Locally scan images during development
 ## Beyond image building
 * Docker port socket and TCP protection
 * Sign images and verify signatures
 * Tag mutability
 * Run as non root
 *  Include health / liveness checks
 *  Drop capabilities

Reference: https://sysdig.com/blog/dockerfile-best-practices/
