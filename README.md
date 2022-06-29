# f5.gitlab.runners

Deploy GitLab runners in local Docker environment

---
Installs runner based on documentation found at https://docs.gitlab.com/runner/install/index.html
---
Register runner following documentation found at https://docs.gitlab.com/runner/register/index.html

Must run following command to register runner. Token is obtained from GitLab.

curl --request POST "https://gitlab.com/api/v4/runners" --form "token=" --form "description=Macbook-Docker-Runner" --form "tag_list=MacOS, Docker, F5-Group"
---
Advanced configuraiton of comfig.toml can be found at https://docs.gitlab.com/runner/configuration/advanced-configuration.html
---
Troubleshooting

Attempt to verify runner is working with "gitlab-runner verify" command

Additional troubleshooting can be found at https://docs.gitlab.com/runner/faq/