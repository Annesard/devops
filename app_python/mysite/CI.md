# Git Actions CI best practices

* Using Self-Hosted Runners in GitHub Actions Workflows: while self-hosting runners increases your operational overhead, there are two big advantages in choosing this option: free runner minutes and increased security.
* Leveraging GitHub Actions Marketplace
* Handling Uncertified Actions
* Managing GitHub Actions Secrets
* Self-Hosted Private Runner Reusability and Storage Challenges

Reference: https://cloud.netapp.com/blog/cvo-blg-5-github-actions-cicd-best-practices

# Jenkins Best Practices

* Always secure Jenkins.
* In larger systems, don't build on the master.
* Backup Jenkins Home regularly.
* Limit project names to a sane (e.g. alphanumeric) character set
* Use "file fingerprinting" to manage dependencies.
* The most reliable builds will be clean builds, which are built fully from Source Code Control.
* Integrate tightly with your issue tracking system, like JIRA or bugzilla, to reduce the need for maintaining a Change Log
* Integrate tightly with a repository browsing tool like FishEye if you are using Subversion as source code management tool
* Set up Jenkins on the partition that has the most free disk-space
* Archive unused jobs before removing them.
* Setup a different job/project for each maintenance or development branch you create
* Prevent resource collisions in jobs that are running in parallel.
* Avoid scheduling all jobs to start at the same time
* Set up email notifications mapping to ALL developers in the project, so that everyone on the team has his pulse on the project's current status.
* Take steps to ensure failures are reported as soon as possible.
* Write jobs for your maintenance tasks, such as cleanup operations to avoid full disk problems.
* Tag, label, or baseline the codebase after the successful build.

Reference: https://wiki.jenkins.io/display/jenkins/jenkins+best+practices
